import asyncio
import logging
from typing import List, Union

import requests
from aiohttp import ClientSession
from empiric.core.entry import SpotEntry
from empiric.core.utils import currency_pair_to_pair_id
from empiric.publisher.assets import EmpiricAsset, EmpiricSpotAsset
from empiric.publisher.types import PublisherFetchError, PublisherInterfaceT

logger = logging.getLogger(__name__)


class OkxFetcher(PublisherInterfaceT):
    BASE_URL: str = "https://okx.com/api/v5/market/ticker"
    SOURCE: str = "OKX"

    publisher: str

    def __init__(self, assets: List[EmpiricAsset], publisher):
        self.assets = assets
        self.publisher = publisher

    async def _fetch_pair(
        self, asset: EmpiricSpotAsset, session: ClientSession
    ) -> Union[SpotEntry, PublisherFetchError]:
        pair = asset["pair"]
        url = f"{self.BASE_URL}?instId={pair[0]}-{pair[1]}-SWAP"

        async with session.get(url) as resp:
            if resp.status == 404:
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from OKX"
                )
            result = await resp.json(content_type="application/json")
            if (
                result["code"] == "51001"
                or result["msg"] == "Instrument ID does not exist"
            ):
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from OKX"
                )

            return self._construct(asset, result)

    def _fetch_pair_sync(
        self, asset: EmpiricSpotAsset
    ) -> Union[SpotEntry, PublisherFetchError]:
        pair = asset["pair"]
        url = f"{self.BASE_URL}?instId={pair[0]}-{pair[1]}-SWAP"

        resp = requests.get(url)
        if resp.status_code == 404:
            return PublisherFetchError(f"No data found for {'/'.join(pair)} from OKX")
        result = resp.json(content_type="application/json")
        if result["code"] == "51001" or result["msg"] == "Instrument ID does not exist":
            return PublisherFetchError(f"No data found for {'/'.join(pair)} from OKX")

        return self._construct(asset, result)

    async def fetch(
        self, session: ClientSession
    ) -> List[Union[SpotEntry, PublisherFetchError]]:
        entries = []
        for asset in self.assets:
            if asset["type"] != "SPOT":
                logger.debug(f"Skipping OKX for non-spot asset {asset}")
                continue
            entries.append(asyncio.ensure_future(self._fetch_pair(asset, session)))
        return await asyncio.gather(*entries, return_exceptions=True)

    def fetch_sync(self) -> List[Union[SpotEntry, PublisherFetchError]]:
        entries = []
        for asset in self.assets:
            if asset["type"] != "SPOT":
                logger.debug(f"Skipping OKX for non-spot asset {asset}")
                continue
            entries.append(self._fetch_pair_sync(asset))
        return entries

    def _construct(self, asset, result) -> SpotEntry:
        pair = asset["pair"]
        data = result["data"][0]

        timestamp = int(data["ts"])
        price = float(data["last"])
        price_int = int(price * (10 ** asset["decimals"]))
        pair_id = currency_pair_to_pair_id(*pair)
        volume = float(data["volCcy24h"])
        volume_int = int(volume)

        logger.info(f"Fetched price {price} for {'/'.join(pair)} from OKX")

        return SpotEntry(
            pair_id=pair_id,
            price=price_int,
            volume=volume_int,
            timestamp=timestamp,
            source=self.SOURCE,
            publisher=self.publisher,
        )

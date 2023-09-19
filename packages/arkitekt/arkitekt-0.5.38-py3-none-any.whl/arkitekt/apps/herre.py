from herre.herre import Herre
from fakts import Fakts
from herre.grants import CacheGrant as HerreCacheGrant
from herre.grants.oauth2.refresh import RefreshGrant
from herre.fakts.fakts_endpoint_fetcher import FaktsUserFetcher
from herre.fakts.grant import FaktsGrant
from typing import Optional
from arkitekt.model import Manifest, User


class ArkitektHerre(Herre):
    pass


def build_arkitekt_herre(
    manifest: Manifest, fakts: Fakts, url: str, no_cache: Optional[bool] = False
) -> ArkitektHerre:
    identifier = manifest.identifier
    version = manifest.version

    return ArkitektHerre(
        grant=RefreshGrant(
            grant=HerreCacheGrant(
                cache_file=f".arkitekt/cache/{identifier}-{version}_herre_cache.json",
                hash=f"{identifier}-{version}-{url}",
                skip_cache=no_cache,
                grant=FaktsGrant(fakts=fakts, fakts_group="lok"),
            ),
        ),
        fetcher=FaktsUserFetcher(
            fakts=fakts, fakts_key="lok.userinfo_url", userModel=User
        ),
    )

import pystac

from api.models import Opportunity, OpportunityCollection, Product, Provider, Search

STAC_ITEM_URL = (
    "https://raw.githubusercontent.com/stac-utils/pystac/main/"
    "tests/data-files/item/sample-item.json"
)


class FakeBackend:
    async def find_opportunities(
        self,
        search: Search,
        token: str,
    ) -> OpportunityCollection:
        item = pystac.Item.from_file(STAC_ITEM_URL)
        opportunity = Opportunity(geometry=item.geometry, properties=item.properties)
        opportunity_collection = OpportunityCollection(features=[opportunity])
        return opportunity_collection

    async def find_products(self, token: str) -> list[Product]:
        # todo: get real list of products
        # todo: consider proper reactions for all types of products
        return [
            Product(
                type="Product",
                stat_version="0.0.1",
                stat_extensions=[],
                id="fake product",
                title="fake product",
                description="",
                license="",
                links=[],
                keywords=[],
                providers=[Provider(name="fake")],
                constraints={},
                parameters={},
            )
        ]

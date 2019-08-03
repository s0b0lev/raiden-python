from raiden_client.endpoints.address import Address


def test_address() -> None:
    address = Address()
    assert address.endpoint == "/address"
    assert address.method == "get"
    assert not address.payload()

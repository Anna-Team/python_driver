from annadb import root, keep


class TestProject:
    def test_keep(self, collection, objects):
        resp = collection.find().sort(+root.name).project(
            {"name": keep, "d": keep}
        ).run()
        for i, (k, v) in enumerate(resp.data.items()):
            assert set(v._value.keys()) == {"name", "d"}
            assert v["name"] == f"test_{i}"
            assert v["d"] == {"smth": i, "smth2": 2}

    def test_set_by_path(self, collection, objects):
        resp = collection.find().sort(+root.name).project(
            {"name": root.smth}
        ).run()
        for i, (k, v) in enumerate(resp.data.items()):
            assert set(v._value.keys()) == {"name"}
            assert v["name"] == "TEST"

    def test_set_value_primitive(self, collection, objects):
        resp = collection.find().sort(+root.name).project(
            {"name": "NEW VALUE"}
        ).run()
        for i, (k, v) in enumerate(resp.data.items()):
            assert set(v._value.keys()) == {"name"}
            assert v["name"] == "NEW VALUE"

    def test_set_value_map(self, collection, objects):
        resp = collection.find().sort(+root.name).project(
            {
                "name": {
                    "test": root.smth
                },
                "d": {
                    "smth2": keep
                }
            }
        ).run()
        for i, (k, v) in enumerate(resp.data.items()):
            assert set(v._value.keys()) == {"name", "d"}
            assert v["name"] == {"test": "TEST"}
            assert v["d"] == {"smth2": 2}

    def test_set_value_vector(self, collection, objects):
        resp = collection.find().sort(+root.name).project(
            {
                "name": [root.smth],
                "l": ["TEST", keep, keep]
            }
        ).run()
        for i, (k, v) in enumerate(resp.data.items()):
            assert set(v._value.keys()) == {"name", "l"}
            assert v["name"] == ["TEST"]
            assert v["l"] == ["TEST", 8, 7]

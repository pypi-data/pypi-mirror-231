import unittest
from resumer.gen.filter import ResumerFilter
from resumer.gen.data import ResumerData

class T_data(unittest.TestCase):
    def test_1(self):
        data = ResumerData()
        data.append(
            a=1,
            b=2,
            exp=[
                {"tags":["a"], "a" : 1, "b" : 2},
                {"a" : 3, "b" : 5},
            ],
            exp2=[
                {"text" : "hello {xxx:world}"},
            ],
            wwa= [
                {"tags" :["b"],"data" : 0x00432},
            ]
        )

        res = data.format(ResumerFilter(
            excludes=["a", "wwa.b"],
            includes=["^xxx"]
        ))
        

        self.assertEqual(
            res,
            {
                "b" :2,
                "exp" : [
                    {"a" : 3, "b" : 5}
                ],
                "exp2" : [
                    {"text" : "hello world"}
                ],
            }
        )


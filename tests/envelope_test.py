import unittest
from nose_parameterized import parameterized

from envelope import Envelope


class EnvelopeTestList(unittest.TestCase):

    @parameterized.expand([
        ["Cant put by square test", Envelope(4, 4), Envelope(1, 7), False],
        ["Cant put by rotation test", Envelope(5, 4), Envelope(5.3, 3), False],
        ["Can put by sides test", Envelope(4, 4), Envelope(2, 2), True],
        ["Can put_by_rotation test", Envelope(5, 4), Envelope(5.1, 1), True],
    ])
    def test_can_put_other(self, name, env1, env2, exp_res):
        act_res = env1.can_put_other(env2)
        try:
            self.assertEqual(act_res, exp_res)
        except AssertionError as e:
            msg ="\nFail test - \"{0}\";\n Input data - {1}; Error{2}".format(name, (env1, env2), e)
            raise AssertionError(msg)

    @parameterized.expand([
        ["Calc_rotation_angle_for_other can_put", Envelope(5, 4), Envelope(5.1, 1.4), 6.872966141183958],
        ["Calc_rotation_angle_for_other can't put", Envelope(5, 4), Envelope(5.1, 1.5), 6.848897994081739],
    ])
    def test_calc_rotation_angle(self, name, env1, env2, exp_res):
        act_res = env1.calc_rotation_angle_for_other(env2)
        try:
            self.assertEqual(act_res, exp_res)
        except AssertionError as e:
            msg = "\nFail test - \"{0}\";\n Input data - {1}; Error{2}".format(name, (env1, env2), e)
            raise AssertionError(msg)


if __name__ == '__main__':
        unittest.main()

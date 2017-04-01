# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from truth import Truth

class TestTruth:

    def test_basic_customization(self):
        # init
        assert Truth
        assert Truth()
        assert Truth('any', 'arguments', (2,3,4), dir(type))

        _ = Truth()

        # repr
        assert repr(_) == '<class Truth>'

        # str
        assert str(_) == '<class Truth>'

        # TODO: bytes
        assert bytes(_) == b'<class Truth>'

        # format
        assert format(_) == '<class Truth>'


    def test_ordering(self):
        _ = Truth()

        assert _ < 7
        assert _ < True
        assert _ < Truth
        assert _ < Truth()

        assert _ <= 7
        assert _ <= True
        assert _ <= Truth
        assert _ <= Truth()

        assert _ == 7
        assert _ == True
        assert _ == Truth
        assert _ == Truth()

        assert _ != 7
        assert _ != True
        assert _ != Truth
        assert _ != Truth()

        assert _ > 7
        assert _ > True
        assert _ > Truth
        assert _ > Truth()

        assert _ <= 7
        assert _ <= True
        assert _ <= Truth
        assert _ <= Truth()

        assert hash(_)
        assert hash(_) == True

        assert bool(_) == True


    def test_attribute_access(self):
        _ = Truth()
        assert _.any_method() == True

        _.any_other_method = lambda x: False
        assert _.any_other_method() == True

        del _.yet_another_method
        assert _.yet_another_method() == True

        # Truth is returned, which means ordering rules work!
        assert _.final_method() != True
        assert _.final_method() == True
        assert _.final_method() < True
        assert _.final_method() > True

        assert repr(_.final_method()) == '<class Truth>'


    def test_callable(self):
        assert Truth
        assert Truth()
        assert Truth()()
        assert Truth('any', 'arguments')('=')(true=True)


    def test_container(self):
        _ = Truth()

        assert len(_)

        assert _[1]
        assert _[3:4]
        _[0] = False
        assert _[0]

        del _[3]
        assert _[3]

        for x in _:
            assert x



    def test_numeric_types(self):
        pass

    def test_context_manager(self):
        pass

    def test_awaitable(self):
        pass

    def test_asynchronous_iterators(self):
        pass

    def test_asynchronous_context_managers(self):
        pass

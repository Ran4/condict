#!/usr/bin/env python3
from unittest import TestCase

import condict
from condict import (
    when,
)

class WhenTest(TestCase):
    def test_empty(self):
        self.assertEqual({
                **when(False, {})
            },
            {
            })
            
    def test_empty2(self):
        user_id = 42
        
        self.assertEqual({
                **when(False, {"user_id": user_id})
            },
            {
            })
            
    def test_on_true_condition(self):
        user_id = 42
        
        self.assertEqual({
                **when(user_id, {"user_id": user_id})
            },
            {
                "user_id": 42,
            })
            
    def test_on_true_condition_with_mandatory_element(self):
        user_id = 42
        
        self.assertEqual({
                "mandatory": "element",
                **when(user_id, {"user_id": user_id})
            },
            {
                "mandatory": "element",
                "user_id": 42,
            })

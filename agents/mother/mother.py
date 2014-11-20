#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant - https://github.com/guluc3m/gul-zoe
#
# Copyright (c) 2014 David Muñoz Díaz <david@gul.es> 
#
# This file is distributed under the MIT LICENSE
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import zoe
from zoe.deco import *
import os
import configparser
import random

CONFIG_FILE = os.path.join(os.environ["ZOE_HOME"], "etc", "zoe-mother.conf")

CHANNELS = ["mail", "jabber"]

MOTHERS_GREATEST_HITS = """
¿Tienes hambre? ¿Te frío un huevo?
Abrígate que hace frío
Esa chica no te traerá más que disgustos
Hazme caso que soy tu madre
Bébete el zumo que se le van las vitaminas
No-me-no-me que-te-que-te
El día que yo no esté ya dirás ¡ay! ¡qué razón tenía!
Estás muy delgado
""".strip().split("\n")

@Agent("mother")
class Agent:

    @Timed(10)
    def update(self):
        ret = []
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        users = config["mother"]["users"].split(",")
        phrase = random.choice(MOTHERS_GREATEST_HITS)
        channel = random.choice(CHANNELS)
        for user in users:
            msg = zoe.MessageBuilder({"src":"mother", "dst":"broadcast", "to":user, "by":channel, "msg":phrase, "tag":"send"})
            ret.append(msg)
        return ret


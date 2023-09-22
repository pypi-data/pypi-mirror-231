# coding: UTF-8
import sys
bstack1l1lll111_opy_ = sys.version_info [0] == 2
bstack11lll111_opy_ = 2048
bstack1ll1l1l11_opy_ = 7
def bstack1l1llll1l_opy_ (bstack1l1ll1l1_opy_):
    global bstack1l111l1l_opy_
    bstack1111l1l1_opy_ = ord (bstack1l1ll1l1_opy_ [-1])
    bstack1l1ll1l_opy_ = bstack1l1ll1l1_opy_ [:-1]
    bstack1l1l111ll_opy_ = bstack1111l1l1_opy_ % len (bstack1l1ll1l_opy_)
    bstack1ll1l11ll_opy_ = bstack1l1ll1l_opy_ [:bstack1l1l111ll_opy_] + bstack1l1ll1l_opy_ [bstack1l1l111ll_opy_:]
    if bstack1l1lll111_opy_:
        bstack1l11ll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll111_opy_ - (bstack1111l_opy_ + bstack1111l1l1_opy_) % bstack1ll1l1l11_opy_) for bstack1111l_opy_, char in enumerate (bstack1ll1l11ll_opy_)])
    else:
        bstack1l11ll1ll_opy_ = str () .join ([chr (ord (char) - bstack11lll111_opy_ - (bstack1111l_opy_ + bstack1111l1l1_opy_) % bstack1ll1l1l11_opy_) for bstack1111l_opy_, char in enumerate (bstack1ll1l11ll_opy_)])
    return eval (bstack1l11ll1ll_opy_)
import atexit
import os
import signal
import sys
import time
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
from multiprocessing import Pool
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
bstack1ll11llll_opy_ = {
	bstack1l1llll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ࠀ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡳࠩࠁ"),
  bstack1l1llll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩࠂ"): bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡫ࡦࡻࠪࠃ"),
  bstack1l1llll1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫࠄ"): bstack1l1llll1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ࠅ"),
  bstack1l1llll1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪࠆ"): bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫࡟ࡸ࠵ࡦࠫࠇ"),
  bstack1l1llll1l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪࠈ"): bstack1l1llll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࠧࠉ"),
  bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪࠊ"): bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧࠋ"),
  bstack1l1llll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࠌ"): bstack1l1llll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨࠍ"),
  bstack1l1llll1l_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪࠎ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩࠪࠏ"),
  bstack1l1llll1l_opy_ (u"࠭ࡣࡰࡰࡶࡳࡱ࡫ࡌࡰࡩࡶࠫࠐ"): bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡶࡳࡱ࡫ࠧࠑ"),
  bstack1l1llll1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ࠒ"): bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡎࡲ࡫ࡸ࠭ࠓ"),
  bstack1l1llll1l_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧࠔ"): bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡵࡶࡩࡶ࡯ࡏࡳ࡬ࡹࠧࠕ"),
  bstack1l1llll1l_opy_ (u"ࠬࡼࡩࡥࡧࡲࠫࠖ"): bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡼࡩࡥࡧࡲࠫࠗ"),
  bstack1l1llll1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭࠘"): bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡎࡲ࡫ࡸ࠭࠙"),
  bstack1l1llll1l_opy_ (u"ࠩࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩࠚ"): bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡷࡩࡱ࡫࡭ࡦࡶࡵࡽࡑࡵࡧࡴࠩࠛ"),
  bstack1l1llll1l_opy_ (u"ࠫ࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩࠜ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡯ࡍࡱࡦࡥࡹ࡯࡯࡯ࠩࠝ"),
  bstack1l1llll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨࠞ"): bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡴࡪ࡯ࡨࡾࡴࡴࡥࠨࠟ"),
  bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪࠠ"): bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫࠡ"),
  bstack1l1llll1l_opy_ (u"ࠪࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩࠢ"): bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡱࡦࡹ࡫ࡄࡱࡰࡱࡦࡴࡤࡴࠩࠣ"),
  bstack1l1llll1l_opy_ (u"ࠬ࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪࠤ"): bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡯ࡤ࡭ࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪࠥ"),
  bstack1l1llll1l_opy_ (u"ࠧ࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧࠦ"): bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡮ࡣࡶ࡯ࡇࡧࡳࡪࡥࡄࡹࡹ࡮ࠧࠧ"),
  bstack1l1llll1l_opy_ (u"ࠩࡶࡩࡳࡪࡋࡦࡻࡶࠫࠨ"): bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡶࡩࡳࡪࡋࡦࡻࡶࠫࠩ"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ࠪ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡙ࡤ࡭ࡹ࠭ࠫ"),
  bstack1l1llll1l_opy_ (u"࠭ࡨࡰࡵࡷࡷࠬࠬ"): bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡨࡰࡵࡷࡷࠬ࠭"),
  bstack1l1llll1l_opy_ (u"ࠨࡤࡩࡧࡦࡩࡨࡦࠩ࠮"): bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡩࡧࡦࡩࡨࡦࠩ࠯"),
  bstack1l1llll1l_opy_ (u"ࠪࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ࠰"): bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡻࡸࡒ࡯ࡤࡣ࡯ࡗࡺࡶࡰࡰࡴࡷࠫ࠱"),
  bstack1l1llll1l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ࠲"): bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ࠳"),
  bstack1l1llll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ࠴"): bstack1l1llll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࠵"),
  bstack1l1llll1l_opy_ (u"ࠩࡵࡩࡦࡲࡍࡰࡤ࡬ࡰࡪ࠭࠶"): bstack1l1llll1l_opy_ (u"ࠪࡶࡪࡧ࡬ࡠ࡯ࡲࡦ࡮ࡲࡥࠨ࠷"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡶࡰࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ࠸"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡶࡰࡪࡷࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࠹"),
  bstack1l1llll1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭࠺"): bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡶࡵࡷࡳࡲࡔࡥࡵࡹࡲࡶࡰ࠭࠻"),
  bstack1l1llll1l_opy_ (u"ࠨࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ࠼"): bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡰࡨࡸࡼࡵࡲ࡬ࡒࡵࡳ࡫࡯࡬ࡦࠩ࠽"),
  bstack1l1llll1l_opy_ (u"ࠪࡥࡨࡩࡥࡱࡶࡌࡲࡸ࡫ࡣࡶࡴࡨࡇࡪࡸࡴࡴࠩ࠾"): bstack1l1llll1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡗࡸࡲࡃࡦࡴࡷࡷࠬ࠿"),
  bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧࡀ"): bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧࡁ"),
  bstack1l1llll1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧࡂ"): bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡴࡱࡸࡶࡨ࡫ࠧࡃ"),
  bstack1l1llll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࡄ"): bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࡅ"),
  bstack1l1llll1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࡆ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ࡇ"),
}
bstack1l11l1l_opy_ = [
  bstack1l1llll1l_opy_ (u"࠭࡯ࡴࠩࡈ"),
  bstack1l1llll1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪࡉ"),
  bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪࡊ"),
  bstack1l1llll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧࡋ"),
  bstack1l1llll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧࡌ"),
  bstack1l1llll1l_opy_ (u"ࠫࡷ࡫ࡡ࡭ࡏࡲࡦ࡮ࡲࡥࠨࡍ"),
  bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡱ࡫ࡸࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬࡎ"),
]
bstack1l1111l1l_opy_ = {
  bstack1l1llll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨࡏ"): [bstack1l1llll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨࡐ"), bstack1l1llll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡤࡔࡁࡎࡇࠪࡑ")],
  bstack1l1llll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬࡒ"): bstack1l1llll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ࡓ"),
  bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧࡔ"): bstack1l1llll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠨࡕ"),
  bstack1l1llll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫࡖ"): bstack1l1llll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡏࡃࡐࡉࠬࡗ"),
  bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࡘ"): bstack1l1llll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࡙ࠫ"),
  bstack1l1llll1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯࡚ࠪ"): bstack1l1llll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡆࡘࡁࡍࡎࡈࡐࡘࡥࡐࡆࡔࡢࡔࡑࡇࡔࡇࡑࡕࡑ࡛ࠬ"),
  bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ࡜"): bstack1l1llll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࠫ࡝"),
  bstack1l1llll1l_opy_ (u"ࠧࡳࡧࡵࡹࡳ࡚ࡥࡴࡶࡶࠫ࡞"): bstack1l1llll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬ࡟"),
  bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵ࠭ࡠ"): [bstack1l1llll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡔࡕࡥࡉࡅࠩࡡ"), bstack1l1llll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡕࡖࠧࡢ")],
  bstack1l1llll1l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧࡣ"): bstack1l1llll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡕࡂࡔࡇࡕ࡚ࡆࡈࡉࡍࡋࡗ࡝ࡤࡊࡅࡃࡗࡊࠫࡤ"),
  bstack1l1llll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫࡥ"): bstack1l1llll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫࡦ")
}
bstack111111l_opy_ = {
  bstack1l1llll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫࡧ"): [bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡸࡷࡪࡸ࡟࡯ࡣࡰࡩࠬࡨ"), bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࡩ")],
  bstack1l1llll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨࡪ"): [bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷࡤࡱࡥࡺࠩ࡫"), bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ࡬")],
  bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ࡭"): bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ࡮"),
  bstack1l1llll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ࡯"): bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨࡰ"),
  bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࡱ"): bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࡲ"),
  bstack1l1llll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧࡳ"): [bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡱࡲࡳࠫࡴ"), bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨࡵ")],
  bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧࡶ"): bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩࡷ"),
  bstack1l1llll1l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩࡸ"): bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡸࡥࡳࡷࡱࡘࡪࡹࡴࡴࠩࡹ"),
  bstack1l1llll1l_opy_ (u"ࠧࡢࡲࡳࠫࡺ"): bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡲࡳࠫࡻ"),
  bstack1l1llll1l_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫࡼ"): bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫࡽ"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨࡾ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨࡿ")
}
bstack1ll11ll_opy_ = {
  bstack1l1llll1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩࢀ"): bstack1l1llll1l_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫࢁ"),
  bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࡙ࡩࡷࡹࡩࡰࡰࠪࢂ"): [bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡵࡨࡰࡪࡴࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫࢃ"), bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ࢄ")],
  bstack1l1llll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩࢅ"): bstack1l1llll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪࢆ"),
  bstack1l1llll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪࢇ"): bstack1l1llll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࢈"),
  bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ࢉ"): [bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪࢊ"), bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩࢋ")],
  bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬࢌ"): bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧࢍ"),
  bstack1l1llll1l_opy_ (u"࠭ࡲࡦࡣ࡯ࡑࡴࡨࡩ࡭ࡧࠪࢎ"): bstack1l1llll1l_opy_ (u"ࠧࡳࡧࡤࡰࡤࡳ࡯ࡣ࡫࡯ࡩࠬ࢏"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ࢐"): [bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡳࡴ࡮ࡻ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࢑"), bstack1l1llll1l_opy_ (u"ࠪࡥࡵࡶࡩࡶ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠫ࢒")],
  bstack1l1llll1l_opy_ (u"ࠫࡦࡩࡣࡦࡲࡷࡍࡳࡹࡥࡤࡷࡵࡩࡈ࡫ࡲࡵࡵࠪ࢓"): [bstack1l1llll1l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡘࡹ࡬ࡄࡧࡵࡸࡸ࠭࢔"), bstack1l1llll1l_opy_ (u"࠭ࡡࡤࡥࡨࡴࡹ࡙ࡳ࡭ࡅࡨࡶࡹ࠭࢕")]
}
bstack11l11l1_opy_ = [
  bstack1l1llll1l_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸ࠭࢖"),
  bstack1l1llll1l_opy_ (u"ࠨࡲࡤ࡫ࡪࡒ࡯ࡢࡦࡖࡸࡷࡧࡴࡦࡩࡼࠫࢗ"),
  bstack1l1llll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ࢘"),
  bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡺࡗࡪࡰࡧࡳࡼࡘࡥࡤࡶ࢙ࠪ"),
  bstack1l1llll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࢚࠭"),
  bstack1l1llll1l_opy_ (u"ࠬࡹࡴࡳ࡫ࡦࡸࡋ࡯࡬ࡦࡋࡱࡸࡪࡸࡡࡤࡶࡤࡦ࡮ࡲࡩࡵࡻ࢛ࠪ"),
  bstack1l1llll1l_opy_ (u"࠭ࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࡒࡵࡳࡲࡶࡴࡃࡧ࡫ࡥࡻ࡯࡯ࡳࠩ࢜"),
  bstack1l1llll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ࢝"),
  bstack1l1llll1l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭࢞"),
  bstack1l1llll1l_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ࢟"),
  bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢠ"),
  bstack1l1llll1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬࢡ"),
]
bstack11ll1ll1l_opy_ = [
  bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩࢢ"),
  bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢣ"),
  bstack1l1llll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ࢤ"),
  bstack1l1llll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨࢥ"),
  bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࢦ"),
  bstack1l1llll1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬࢧ"),
  bstack1l1llll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧࢨ"),
  bstack1l1llll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩࢩ"),
  bstack1l1llll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩࢪ"),
  bstack1l1llll1l_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬࢫ")
]
bstack1l111l_opy_ = [
  bstack1l1llll1l_opy_ (u"ࠨࡷࡳࡰࡴࡧࡤࡎࡧࡧ࡭ࡦ࠭ࢬ"),
  bstack1l1llll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫࢭ"),
  bstack1l1llll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ࢮ"),
  bstack1l1llll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩࢯ"),
  bstack1l1llll1l_opy_ (u"ࠬࡺࡥࡴࡶࡓࡶ࡮ࡵࡲࡪࡶࡼࠫࢰ"),
  bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩࢱ"),
  bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࡚ࡡࡨࠩࢲ"),
  bstack1l1llll1l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ࢳ"),
  bstack1l1llll1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࡚ࡪࡸࡳࡪࡱࡱࠫࢴ"),
  bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨࢵ"),
  bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬࢶ"),
  bstack1l1llll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫࢷ"),
  bstack1l1llll1l_opy_ (u"࠭࡯ࡴࠩࢸ"),
  bstack1l1llll1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪࢹ"),
  bstack1l1llll1l_opy_ (u"ࠨࡪࡲࡷࡹࡹࠧࢺ"),
  bstack1l1llll1l_opy_ (u"ࠩࡤࡹࡹࡵࡗࡢ࡫ࡷࠫࢻ"),
  bstack1l1llll1l_opy_ (u"ࠪࡶࡪ࡭ࡩࡰࡰࠪࢼ"),
  bstack1l1llll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡼࡲࡲࡪ࠭ࢽ"),
  bstack1l1llll1l_opy_ (u"ࠬࡳࡡࡤࡪ࡬ࡲࡪ࠭ࢾ"),
  bstack1l1llll1l_opy_ (u"࠭ࡲࡦࡵࡲࡰࡺࡺࡩࡰࡰࠪࢿ"),
  bstack1l1llll1l_opy_ (u"ࠧࡪࡦ࡯ࡩ࡙࡯࡭ࡦࡱࡸࡸࠬࣀ"),
  bstack1l1llll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡐࡴ࡬ࡩࡳࡺࡡࡵ࡫ࡲࡲࠬࣁ"),
  bstack1l1llll1l_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࠨࣂ"),
  bstack1l1llll1l_opy_ (u"ࠪࡲࡴࡖࡡࡨࡧࡏࡳࡦࡪࡔࡪ࡯ࡨࡳࡺࡺࠧࣃ"),
  bstack1l1llll1l_opy_ (u"ࠫࡧ࡬ࡣࡢࡥ࡫ࡩࠬࣄ"),
  bstack1l1llll1l_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫࣅ"),
  bstack1l1llll1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲ࡙ࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪࣆ"),
  bstack1l1llll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡓࡦࡰࡧࡏࡪࡿࡳࠨࣇ"),
  bstack1l1llll1l_opy_ (u"ࠨࡴࡨࡥࡱࡓ࡯ࡣ࡫࡯ࡩࠬࣈ"),
  bstack1l1llll1l_opy_ (u"ࠩࡱࡳࡕ࡯ࡰࡦ࡮࡬ࡲࡪ࠭ࣉ"),
  bstack1l1llll1l_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬ࡗࡕࡐࠬ࣊"),
  bstack1l1llll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣋"),
  bstack1l1llll1l_opy_ (u"ࠬࡧࡣࡤࡧࡳࡸࡈࡵ࡯࡬࡫ࡨࡷࠬ࣌"),
  bstack1l1llll1l_opy_ (u"࠭ࡣࡢࡲࡷࡹࡷ࡫ࡃࡳࡣࡶ࡬ࠬ࣍"),
  bstack1l1llll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ࣎"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡳࡴ࡮ࡻ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ࣏"),
  bstack1l1llll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࡜ࡥࡳࡵ࡬ࡳࡳ࣐࠭"),
  bstack1l1llll1l_opy_ (u"ࠪࡲࡴࡈ࡬ࡢࡰ࡮ࡔࡴࡲ࡬ࡪࡰࡪ࣑ࠫ"),
  bstack1l1llll1l_opy_ (u"ࠫࡲࡧࡳ࡬ࡕࡨࡲࡩࡑࡥࡺࡵ࣒ࠪ"),
  bstack1l1llll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡑࡵࡧࡴ࣓ࠩ"),
  bstack1l1llll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡏࡤࠨࣔ"),
  bstack1l1llll1l_opy_ (u"ࠧࡥࡧࡧ࡭ࡨࡧࡴࡦࡦࡇࡩࡻ࡯ࡣࡦࠩࣕ"),
  bstack1l1llll1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡑࡣࡵࡥࡲࡹࠧࣖ"),
  bstack1l1llll1l_opy_ (u"ࠩࡳ࡬ࡴࡴࡥࡏࡷࡰࡦࡪࡸࠧࣗ"),
  bstack1l1llll1l_opy_ (u"ࠪࡲࡪࡺࡷࡰࡴ࡮ࡐࡴ࡭ࡳࠨࣘ"),
  bstack1l1llll1l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡑࡵࡧࡴࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣙ"),
  bstack1l1llll1l_opy_ (u"ࠬࡩ࡯࡯ࡵࡲࡰࡪࡒ࡯ࡨࡵࠪࣚ"),
  bstack1l1llll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ࣛ"),
  bstack1l1llll1l_opy_ (u"ࠧࡢࡲࡳ࡭ࡺࡳࡌࡰࡩࡶࠫࣜ"),
  bstack1l1llll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡃ࡫ࡲࡱࡪࡺࡲࡪࡥࠪࣝ"),
  bstack1l1llll1l_opy_ (u"ࠩࡹ࡭ࡩ࡫࡯ࡗ࠴ࠪࣞ"),
  bstack1l1llll1l_opy_ (u"ࠪࡱ࡮ࡪࡓࡦࡵࡶ࡭ࡴࡴࡉ࡯ࡵࡷࡥࡱࡲࡁࡱࡲࡶࠫࣟ"),
  bstack1l1llll1l_opy_ (u"ࠫࡪࡹࡰࡳࡧࡶࡷࡴ࡙ࡥࡳࡸࡨࡶࠬ࣠"),
  bstack1l1llll1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࡌࡰࡩࡶࠫ࣡"),
  bstack1l1llll1l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࡄࡦࡳࠫ࣢"),
  bstack1l1llll1l_opy_ (u"ࠧࡵࡧ࡯ࡩࡲ࡫ࡴࡳࡻࡏࡳ࡬ࡹࣣࠧ"),
  bstack1l1llll1l_opy_ (u"ࠨࡵࡼࡲࡨ࡚ࡩ࡮ࡧ࡚࡭ࡹ࡮ࡎࡕࡒࠪࣤ"),
  bstack1l1llll1l_opy_ (u"ࠩࡪࡩࡴࡒ࡯ࡤࡣࡷ࡭ࡴࡴࠧࣥ"),
  bstack1l1llll1l_opy_ (u"ࠪ࡫ࡵࡹࡌࡰࡥࡤࡸ࡮ࡵ࡮ࠨࣦ"),
  bstack1l1llll1l_opy_ (u"ࠫࡳ࡫ࡴࡸࡱࡵ࡯ࡕࡸ࡯ࡧ࡫࡯ࡩࠬࣧ"),
  bstack1l1llll1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡓ࡫ࡴࡸࡱࡵ࡯ࠬࣨ"),
  bstack1l1llll1l_opy_ (u"࠭ࡦࡰࡴࡦࡩࡈ࡮ࡡ࡯ࡩࡨࡎࡦࡸࣩࠧ"),
  bstack1l1llll1l_opy_ (u"ࠧࡹ࡯ࡶࡎࡦࡸࠧ࣪"),
  bstack1l1llll1l_opy_ (u"ࠨࡺࡰࡼࡏࡧࡲࠨ࣫"),
  bstack1l1llll1l_opy_ (u"ࠩࡰࡥࡸࡱࡃࡰ࡯ࡰࡥࡳࡪࡳࠨ࣬"),
  bstack1l1llll1l_opy_ (u"ࠪࡱࡦࡹ࡫ࡃࡣࡶ࡭ࡨࡇࡵࡵࡪ࣭ࠪ"),
  bstack1l1llll1l_opy_ (u"ࠫࡼࡹࡌࡰࡥࡤࡰࡘࡻࡰࡱࡱࡵࡸ࣮ࠬ"),
  bstack1l1llll1l_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡉ࡯ࡳࡵࡕࡩࡸࡺࡲࡪࡥࡷ࡭ࡴࡴࡳࠨ࣯"),
  bstack1l1llll1l_opy_ (u"࠭ࡡࡱࡲ࡙ࡩࡷࡹࡩࡰࡰࣰࠪ"),
  bstack1l1llll1l_opy_ (u"ࠧࡢࡥࡦࡩࡵࡺࡉ࡯ࡵࡨࡧࡺࡸࡥࡄࡧࡵࡸࡸࣱ࠭"),
  bstack1l1llll1l_opy_ (u"ࠨࡴࡨࡷ࡮࡭࡮ࡂࡲࡳࣲࠫ"),
  bstack1l1llll1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡲ࡮ࡳࡡࡵ࡫ࡲࡲࡸ࠭ࣳ"),
  bstack1l1llll1l_opy_ (u"ࠪࡧࡦࡴࡡࡳࡻࠪࣴ"),
  bstack1l1llll1l_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬࣵ"),
  bstack1l1llll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࣶࠬ"),
  bstack1l1llll1l_opy_ (u"࠭ࡩࡦࠩࣷ"),
  bstack1l1llll1l_opy_ (u"ࠧࡦࡦࡪࡩࠬࣸ"),
  bstack1l1llll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨࣹ"),
  bstack1l1llll1l_opy_ (u"ࠩࡴࡹࡪࡻࡥࠨࣺ"),
  bstack1l1llll1l_opy_ (u"ࠪ࡭ࡳࡺࡥࡳࡰࡤࡰࠬࣻ"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡶࡰࡔࡶࡲࡶࡪࡉ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠬࣼ"),
  bstack1l1llll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡈࡧ࡭ࡦࡴࡤࡍࡲࡧࡧࡦࡋࡱ࡮ࡪࡩࡴࡪࡱࡱࠫࣽ"),
  bstack1l1llll1l_opy_ (u"࠭࡮ࡦࡶࡺࡳࡷࡱࡌࡰࡩࡶࡉࡽࡩ࡬ࡶࡦࡨࡌࡴࡹࡴࡴࠩࣾ"),
  bstack1l1llll1l_opy_ (u"ࠧ࡯ࡧࡷࡻࡴࡸ࡫ࡍࡱࡪࡷࡎࡴࡣ࡭ࡷࡧࡩࡍࡵࡳࡵࡵࠪࣿ"),
  bstack1l1llll1l_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡂࡲࡳࡗࡪࡺࡴࡪࡰࡪࡷࠬऀ"),
  bstack1l1llll1l_opy_ (u"ࠩࡵࡩࡸ࡫ࡲࡷࡧࡇࡩࡻ࡯ࡣࡦࠩँ"),
  bstack1l1llll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪं"),
  bstack1l1llll1l_opy_ (u"ࠫࡸ࡫࡮ࡥࡍࡨࡽࡸ࠭ः"),
  bstack1l1llll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡕࡧࡳࡴࡥࡲࡨࡪ࠭ऄ"),
  bstack1l1llll1l_opy_ (u"࠭ࡵࡱࡦࡤࡸࡪࡏ࡯ࡴࡆࡨࡺ࡮ࡩࡥࡔࡧࡷࡸ࡮ࡴࡧࡴࠩअ"),
  bstack1l1llll1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡁࡶࡦ࡬ࡳࡎࡴࡪࡦࡥࡷ࡭ࡴࡴࠧआ"),
  bstack1l1llll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡂࡲࡳࡰࡪࡖࡡࡺࠩइ"),
  bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪई"),
  bstack1l1llll1l_opy_ (u"ࠪࡻࡩ࡯࡯ࡔࡧࡵࡺ࡮ࡩࡥࠨउ"),
  bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ऊ"),
  bstack1l1llll1l_opy_ (u"ࠬࡶࡲࡦࡸࡨࡲࡹࡉࡲࡰࡵࡶࡗ࡮ࡺࡥࡕࡴࡤࡧࡰ࡯࡮ࡨࠩऋ"),
  bstack1l1llll1l_opy_ (u"࠭ࡨࡪࡩ࡫ࡇࡴࡴࡴࡳࡣࡶࡸࠬऌ"),
  bstack1l1llll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡐࡳࡧࡩࡩࡷ࡫࡮ࡤࡧࡶࠫऍ"),
  bstack1l1llll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡔ࡫ࡰࠫऎ"),
  bstack1l1llll1l_opy_ (u"ࠩࡶ࡭ࡲࡕࡰࡵ࡫ࡲࡲࡸ࠭ए"),
  bstack1l1llll1l_opy_ (u"ࠪࡶࡪࡳ࡯ࡷࡧࡌࡓࡘࡇࡰࡱࡕࡨࡸࡹ࡯࡮ࡨࡵࡏࡳࡨࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠨऐ"),
  bstack1l1llll1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ऑ"),
  bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧऒ"),
  bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠨओ"),
  bstack1l1llll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭औ"),
  bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪक"),
  bstack1l1llll1l_opy_ (u"ࠩࡳࡥ࡬࡫ࡌࡰࡣࡧࡗࡹࡸࡡࡵࡧࡪࡽࠬख"),
  bstack1l1llll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩग"),
  bstack1l1llll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡱࡸࡸࡸ࠭घ"),
  bstack1l1llll1l_opy_ (u"ࠬࡻ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡑࡴࡲࡱࡵࡺࡂࡦࡪࡤࡺ࡮ࡵࡲࠨङ")
]
bstack1llll111l_opy_ = {
  bstack1l1llll1l_opy_ (u"࠭ࡶࠨच"): bstack1l1llll1l_opy_ (u"ࠧࡷࠩछ"),
  bstack1l1llll1l_opy_ (u"ࠨࡨࠪज"): bstack1l1llll1l_opy_ (u"ࠩࡩࠫझ"),
  bstack1l1llll1l_opy_ (u"ࠪࡪࡴࡸࡣࡦࠩञ"): bstack1l1llll1l_opy_ (u"ࠫ࡫ࡵࡲࡤࡧࠪट"),
  bstack1l1llll1l_opy_ (u"ࠬࡵ࡮࡭ࡻࡤࡹࡹࡵ࡭ࡢࡶࡨࠫठ"): bstack1l1llll1l_opy_ (u"࠭࡯࡯࡮ࡼࡅࡺࡺ࡯࡮ࡣࡷࡩࠬड"),
  bstack1l1llll1l_opy_ (u"ࠧࡧࡱࡵࡧࡪࡲ࡯ࡤࡣ࡯ࠫढ"): bstack1l1llll1l_opy_ (u"ࠨࡨࡲࡶࡨ࡫࡬ࡰࡥࡤࡰࠬण"),
  bstack1l1llll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡩࡱࡶࡸࠬत"): bstack1l1llll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭थ"),
  bstack1l1llll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡳࡳࡷࡺࠧद"): bstack1l1llll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨध"),
  bstack1l1llll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡺࡹࡥࡳࠩन"): bstack1l1llll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪऩ"),
  bstack1l1llll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡰࡢࡵࡶࠫप"): bstack1l1llll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬफ"),
  bstack1l1llll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡨࡰࡵࡷࠫब"): bstack1l1llll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡉࡱࡶࡸࠬभ"),
  bstack1l1llll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡴࡷࡵࡸࡺࡲࡲࡶࡹ࠭म"): bstack1l1llll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧय"),
  bstack1l1llll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡹࡸ࡫ࡲࠨर"): bstack1l1llll1l_opy_ (u"ࠨ࠯࡯ࡳࡨࡧ࡬ࡑࡴࡲࡼࡾ࡛ࡳࡦࡴࠪऱ"),
  bstack1l1llll1l_opy_ (u"ࠩ࠰ࡰࡴࡩࡡ࡭ࡲࡵࡳࡽࡿࡵࡴࡧࡵࠫल"): bstack1l1llll1l_opy_ (u"ࠪ࠱ࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡖࡵࡨࡶࠬळ"),
  bstack1l1llll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡳࡶࡴࡾࡹࡱࡣࡶࡷࠬऴ"): bstack1l1llll1l_opy_ (u"ࠬ࠳࡬ࡰࡥࡤࡰࡕࡸ࡯ࡹࡻࡓࡥࡸࡹࠧव"),
  bstack1l1llll1l_opy_ (u"࠭࠭࡭ࡱࡦࡥࡱࡶࡲࡰࡺࡼࡴࡦࡹࡳࠨश"): bstack1l1llll1l_opy_ (u"ࠧ࠮࡮ࡲࡧࡦࡲࡐࡳࡱࡻࡽࡕࡧࡳࡴࠩष"),
  bstack1l1llll1l_opy_ (u"ࠨࡤ࡬ࡲࡦࡸࡹࡱࡣࡷ࡬ࠬस"): bstack1l1llll1l_opy_ (u"ࠩࡥ࡭ࡳࡧࡲࡺࡲࡤࡸ࡭࠭ह"),
  bstack1l1llll1l_opy_ (u"ࠪࡴࡦࡩࡦࡪ࡮ࡨࠫऺ"): bstack1l1llll1l_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧऻ"),
  bstack1l1llll1l_opy_ (u"ࠬࡶࡡࡤ࠯ࡩ࡭ࡱ࡫़ࠧ"): bstack1l1llll1l_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩऽ"),
  bstack1l1llll1l_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪा"): bstack1l1llll1l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫि"),
  bstack1l1llll1l_opy_ (u"ࠩ࡯ࡳ࡬࡬ࡩ࡭ࡧࠪी"): bstack1l1llll1l_opy_ (u"ࠪࡰࡴ࡭ࡦࡪ࡮ࡨࠫु"),
  bstack1l1llll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ू"): bstack1l1llll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧृ"),
}
bstack1llllll1_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡸࡦ࠲࡬ࡺࡨࠧॄ")
bstack11ll11lll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡩࡷࡥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠪॅ")
bstack1ll11l1l_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱࡫ࡹࡧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡱࡩࡽࡺ࡟ࡩࡷࡥࡷࠬॆ")
bstack1llll11l_opy_ = {
  bstack1l1llll1l_opy_ (u"ࠩࡦࡶ࡮ࡺࡩࡤࡣ࡯ࠫे"): 50,
  bstack1l1llll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩै"): 40,
  bstack1l1llll1l_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬॉ"): 30,
  bstack1l1llll1l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪॊ"): 20,
  bstack1l1llll1l_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬो"): 10
}
bstack1l11_opy_ = bstack1llll11l_opy_[bstack1l1llll1l_opy_ (u"ࠧࡪࡰࡩࡳࠬौ")]
bstack11l1ll111_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵्ࠧ")
bstack11l11l111_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࠧॎ")
bstack1lll11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࠩॏ")
bstack1l1ll1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࠪॐ")
bstack11lll_opy_ = [bstack1l1llll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭॑"), bstack1l1llll1l_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ॒࠭")]
bstack111ll11_opy_ = [bstack1l1llll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ॓"), bstack1l1llll1l_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ॔")]
bstack111l1_opy_ = [
  bstack1l1llll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡔࡡ࡮ࡧࠪॕ"),
  bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬॖ"),
  bstack1l1llll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨॗ"),
  bstack1l1llll1l_opy_ (u"ࠬࡴࡥࡸࡅࡲࡱࡲࡧ࡮ࡥࡖ࡬ࡱࡪࡵࡵࡵࠩक़"),
  bstack1l1llll1l_opy_ (u"࠭ࡡࡱࡲࠪख़"),
  bstack1l1llll1l_opy_ (u"ࠧࡶࡦ࡬ࡨࠬग़"),
  bstack1l1llll1l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪज़"),
  bstack1l1llll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡦࠩड़"),
  bstack1l1llll1l_opy_ (u"ࠪࡳࡷ࡯ࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠨढ़"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡙ࡨࡦࡻ࡯ࡥࡸࠩफ़"),
  bstack1l1llll1l_opy_ (u"ࠬࡴ࡯ࡓࡧࡶࡩࡹ࠭य़"), bstack1l1llll1l_opy_ (u"࠭ࡦࡶ࡮࡯ࡖࡪࡹࡥࡵࠩॠ"),
  bstack1l1llll1l_opy_ (u"ࠧࡤ࡮ࡨࡥࡷ࡙ࡹࡴࡶࡨࡱࡋ࡯࡬ࡦࡵࠪॡ"),
  bstack1l1llll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺࡔࡪ࡯࡬ࡲ࡬ࡹࠧॢ"),
  bstack1l1llll1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࡒ࡯ࡨࡩ࡬ࡲ࡬࠭ॣ"),
  bstack1l1llll1l_opy_ (u"ࠪࡳࡹ࡮ࡥࡳࡃࡳࡴࡸ࠭।"),
  bstack1l1llll1l_opy_ (u"ࠫࡵࡸࡩ࡯ࡶࡓࡥ࡬࡫ࡓࡰࡷࡵࡧࡪࡕ࡮ࡇ࡫ࡱࡨࡋࡧࡩ࡭ࡷࡵࡩࠬ॥"),
  bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡱࡃࡦࡸ࡮ࡼࡩࡵࡻࠪ०"), bstack1l1llll1l_opy_ (u"࠭ࡡࡱࡲࡓࡥࡨࡱࡡࡨࡧࠪ१"), bstack1l1llll1l_opy_ (u"ࠧࡢࡲࡳ࡛ࡦ࡯ࡴࡂࡥࡷ࡭ࡻ࡯ࡴࡺࠩ२"), bstack1l1llll1l_opy_ (u"ࠨࡣࡳࡴ࡜ࡧࡩࡵࡒࡤࡧࡰࡧࡧࡦࠩ३"), bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵ࡝ࡡࡪࡶࡇࡹࡷࡧࡴࡪࡱࡱࠫ४"),
  bstack1l1llll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡕࡩࡦࡪࡹࡕ࡫ࡰࡩࡴࡻࡴࠨ५"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡗࡩࡸࡺࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠨ६"),
  bstack1l1llll1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩࡉ࡯ࡷࡧࡵࡥ࡬࡫ࠧ७"), bstack1l1llll1l_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࡃࡰࡸࡨࡶࡦ࡭ࡥࡆࡰࡧࡍࡳࡺࡥ࡯ࡶࠪ८"),
  bstack1l1llll1l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࡅࡧࡹ࡭ࡨ࡫ࡒࡦࡣࡧࡽ࡙࡯࡭ࡦࡱࡸࡸࠬ९"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡧࡦࡕࡵࡲࡵࠩ॰"),
  bstack1l1llll1l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡇࡩࡻ࡯ࡣࡦࡕࡲࡧࡰ࡫ࡴࠨॱ"),
  bstack1l1llll1l_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࡍࡳࡹࡴࡢ࡮࡯ࡘ࡮ࡳࡥࡰࡷࡷࠫॲ"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࡎࡴࡳࡵࡣ࡯ࡰࡕࡧࡴࡩࠩॳ"),
  bstack1l1llll1l_opy_ (u"ࠬࡧࡶࡥࠩॴ"), bstack1l1llll1l_opy_ (u"࠭ࡡࡷࡦࡏࡥࡺࡴࡣࡩࡖ࡬ࡱࡪࡵࡵࡵࠩॵ"), bstack1l1llll1l_opy_ (u"ࠧࡢࡸࡧࡖࡪࡧࡤࡺࡖ࡬ࡱࡪࡵࡵࡵࠩॶ"), bstack1l1llll1l_opy_ (u"ࠨࡣࡹࡨࡆࡸࡧࡴࠩॷ"),
  bstack1l1llll1l_opy_ (u"ࠩࡸࡷࡪࡑࡥࡺࡵࡷࡳࡷ࡫ࠧॸ"), bstack1l1llll1l_opy_ (u"ࠪ࡯ࡪࡿࡳࡵࡱࡵࡩࡕࡧࡴࡩࠩॹ"), bstack1l1llll1l_opy_ (u"ࠫࡰ࡫ࡹࡴࡶࡲࡶࡪࡖࡡࡴࡵࡺࡳࡷࡪࠧॺ"),
  bstack1l1llll1l_opy_ (u"ࠬࡱࡥࡺࡃ࡯࡭ࡦࡹࠧॻ"), bstack1l1llll1l_opy_ (u"࠭࡫ࡦࡻࡓࡥࡸࡹࡷࡰࡴࡧࠫॼ"),
  bstack1l1llll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡋࡸࡦࡥࡸࡸࡦࡨ࡬ࡦࠩॽ"), bstack1l1llll1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡥࡴ࡬ࡺࡪࡸࡁࡳࡩࡶࠫॾ"), bstack1l1llll1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡦࡵ࡭ࡻ࡫ࡲࡆࡺࡨࡧࡺࡺࡡࡣ࡮ࡨࡈ࡮ࡸࠧॿ"), bstack1l1llll1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡧࡶ࡮ࡼࡥࡳࡅ࡫ࡶࡴࡳࡥࡎࡣࡳࡴ࡮ࡴࡧࡇ࡫࡯ࡩࠬঀ"), bstack1l1llll1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡨࡷ࡯ࡶࡦࡴࡘࡷࡪ࡙ࡹࡴࡶࡨࡱࡊࡾࡥࡤࡷࡷࡥࡧࡲࡥࠨঁ"),
  bstack1l1llll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡩࡸࡩࡷࡧࡵࡔࡴࡸࡴࠨং"), bstack1l1llll1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡪࡲࡪࡸࡨࡶࡕࡵࡲࡵࡵࠪঃ"),
  bstack1l1llll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࡤࡳ࡫ࡹࡩࡷࡊࡩࡴࡣࡥࡰࡪࡈࡵࡪ࡮ࡧࡇ࡭࡫ࡣ࡬ࠩ঄"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡸࡸࡴ࡝ࡥࡣࡸ࡬ࡩࡼ࡚ࡩ࡮ࡧࡲࡹࡹ࠭অ"),
  bstack1l1llll1l_opy_ (u"ࠩ࡬ࡲࡹ࡫࡮ࡵࡃࡦࡸ࡮ࡵ࡮ࠨআ"), bstack1l1llll1l_opy_ (u"ࠪ࡭ࡳࡺࡥ࡯ࡶࡆࡥࡹ࡫ࡧࡰࡴࡼࠫই"), bstack1l1llll1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡰࡷࡊࡱࡧࡧࡴࠩঈ"), bstack1l1llll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡦࡲࡉ࡯ࡶࡨࡲࡹࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨউ"),
  bstack1l1llll1l_opy_ (u"࠭ࡤࡰࡰࡷࡗࡹࡵࡰࡂࡲࡳࡓࡳࡘࡥࡴࡧࡷࠫঊ"),
  bstack1l1llll1l_opy_ (u"ࠧࡶࡰ࡬ࡧࡴࡪࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩঋ"), bstack1l1llll1l_opy_ (u"ࠨࡴࡨࡷࡪࡺࡋࡦࡻࡥࡳࡦࡸࡤࠨঌ"),
  bstack1l1llll1l_opy_ (u"ࠩࡱࡳࡘ࡯ࡧ࡯ࠩ঍"),
  bstack1l1llll1l_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࡘࡲ࡮ࡳࡰࡰࡴࡷࡥࡳࡺࡖࡪࡧࡺࡷࠬ঎"),
  bstack1l1llll1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡴࡤࡳࡱ࡬ࡨ࡜ࡧࡴࡤࡪࡨࡶࡸ࠭এ"),
  bstack1l1llll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬঐ"),
  bstack1l1llll1l_opy_ (u"࠭ࡲࡦࡥࡵࡩࡦࡺࡥࡄࡪࡵࡳࡲ࡫ࡄࡳ࡫ࡹࡩࡷ࡙ࡥࡴࡵ࡬ࡳࡳࡹࠧ঑"),
  bstack1l1llll1l_opy_ (u"ࠧ࡯ࡣࡷ࡭ࡻ࡫ࡗࡦࡤࡖࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭঒"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡱࡨࡷࡵࡩࡥࡕࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡕࡧࡴࡩࠩও"),
  bstack1l1llll1l_opy_ (u"ࠩࡱࡩࡹࡽ࡯ࡳ࡭ࡖࡴࡪ࡫ࡤࠨঔ"),
  bstack1l1llll1l_opy_ (u"ࠪ࡫ࡵࡹࡅ࡯ࡣࡥࡰࡪࡪࠧক"),
  bstack1l1llll1l_opy_ (u"ࠫ࡮ࡹࡈࡦࡣࡧࡰࡪࡹࡳࠨখ"),
  bstack1l1llll1l_opy_ (u"ࠬࡧࡤࡣࡇࡻࡩࡨ࡚ࡩ࡮ࡧࡲࡹࡹ࠭গ"),
  bstack1l1llll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡪ࡙ࡣࡳ࡫ࡳࡸࠬঘ"),
  bstack1l1llll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡉ࡫ࡶࡪࡥࡨࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠫঙ"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡸࡸࡴࡍࡲࡢࡰࡷࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࡳࠨচ"),
  bstack1l1llll1l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࡑࡥࡹࡻࡲࡢ࡮ࡒࡶ࡮࡫࡮ࡵࡣࡷ࡭ࡴࡴࠧছ"),
  bstack1l1llll1l_opy_ (u"ࠪࡷࡾࡹࡴࡦ࡯ࡓࡳࡷࡺࠧজ"),
  bstack1l1llll1l_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡅࡩࡨࡈࡰࡵࡷࠫঝ"),
  bstack1l1llll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡘࡲࡱࡵࡣ࡬ࠩঞ"), bstack1l1llll1l_opy_ (u"࠭ࡵ࡯࡮ࡲࡧࡰ࡚ࡹࡱࡧࠪট"), bstack1l1llll1l_opy_ (u"ࠧࡶࡰ࡯ࡳࡨࡱࡋࡦࡻࠪঠ"),
  bstack1l1llll1l_opy_ (u"ࠨࡣࡸࡸࡴࡒࡡࡶࡰࡦ࡬ࠬড"),
  bstack1l1llll1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡌࡰࡩࡦࡥࡹࡉࡡࡱࡶࡸࡶࡪ࠭ঢ"),
  bstack1l1llll1l_opy_ (u"ࠪࡹࡳ࡯࡮ࡴࡶࡤࡰࡱࡕࡴࡩࡧࡵࡔࡦࡩ࡫ࡢࡩࡨࡷࠬণ"),
  bstack1l1llll1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩ࡜࡯࡮ࡥࡱࡺࡅࡳ࡯࡭ࡢࡶ࡬ࡳࡳ࠭ত"),
  bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡘࡴࡵ࡬ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩথ"),
  bstack1l1llll1l_opy_ (u"࠭ࡥ࡯ࡨࡲࡶࡨ࡫ࡁࡱࡲࡌࡲࡸࡺࡡ࡭࡮ࠪদ"),
  bstack1l1llll1l_opy_ (u"ࠧࡦࡰࡶࡹࡷ࡫ࡗࡦࡤࡹ࡭ࡪࡽࡳࡉࡣࡹࡩࡕࡧࡧࡦࡵࠪধ"), bstack1l1llll1l_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࡆࡨࡺࡹࡵ࡯࡭ࡵࡓࡳࡷࡺࠧন"), bstack1l1llll1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦ࡙ࡨࡦࡻ࡯ࡥࡸࡆࡨࡸࡦ࡯࡬ࡴࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠬ঩"),
  bstack1l1llll1l_opy_ (u"ࠪࡶࡪࡳ࡯ࡵࡧࡄࡴࡵࡹࡃࡢࡥ࡫ࡩࡑ࡯࡭ࡪࡶࠪপ"),
  bstack1l1llll1l_opy_ (u"ࠫࡨࡧ࡬ࡦࡰࡧࡥࡷࡌ࡯ࡳ࡯ࡤࡸࠬফ"),
  bstack1l1llll1l_opy_ (u"ࠬࡨࡵ࡯ࡦ࡯ࡩࡎࡪࠧব"),
  bstack1l1llll1l_opy_ (u"࠭࡬ࡢࡷࡱࡧ࡭࡚ࡩ࡮ࡧࡲࡹࡹ࠭ভ"),
  bstack1l1llll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࡕࡨࡶࡻ࡯ࡣࡦࡵࡈࡲࡦࡨ࡬ࡦࡦࠪম"), bstack1l1llll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࡖࡩࡷࡼࡩࡤࡧࡶࡅࡺࡺࡨࡰࡴ࡬ࡾࡪࡪࠧয"),
  bstack1l1llll1l_opy_ (u"ࠩࡤࡹࡹࡵࡁࡤࡥࡨࡴࡹࡇ࡬ࡦࡴࡷࡷࠬর"), bstack1l1llll1l_opy_ (u"ࠪࡥࡺࡺ࡯ࡅ࡫ࡶࡱ࡮ࡹࡳࡂ࡮ࡨࡶࡹࡹࠧ঱"),
  bstack1l1llll1l_opy_ (u"ࠫࡳࡧࡴࡪࡸࡨࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡳࡍ࡫ࡥࠫল"),
  bstack1l1llll1l_opy_ (u"ࠬࡴࡡࡵ࡫ࡹࡩ࡜࡫ࡢࡕࡣࡳࠫ঳"),
  bstack1l1llll1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡏ࡮ࡪࡶ࡬ࡥࡱ࡛ࡲ࡭ࠩ঴"), bstack1l1llll1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࡁ࡭࡮ࡲࡻࡕࡵࡰࡶࡲࡶࠫ঵"), bstack1l1llll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࡊࡩࡱࡳࡷ࡫ࡆࡳࡣࡸࡨ࡜ࡧࡲ࡯࡫ࡱ࡫ࠬশ"), bstack1l1llll1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࡑࡳࡩࡳࡒࡩ࡯࡭ࡶࡍࡳࡈࡡࡤ࡭ࡪࡶࡴࡻ࡮ࡥࠩষ"),
  bstack1l1llll1l_opy_ (u"ࠪ࡯ࡪ࡫ࡰࡌࡧࡼࡇ࡭ࡧࡩ࡯ࡵࠪস"),
  bstack1l1llll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮࡬ࡾࡦࡨ࡬ࡦࡕࡷࡶ࡮ࡴࡧࡴࡆ࡬ࡶࠬহ"),
  bstack1l1llll1l_opy_ (u"ࠬࡶࡲࡰࡥࡨࡷࡸࡇࡲࡨࡷࡰࡩࡳࡺࡳࠨ঺"),
  bstack1l1llll1l_opy_ (u"࠭ࡩ࡯ࡶࡨࡶࡐ࡫ࡹࡅࡧ࡯ࡥࡾ࠭঻"),
  bstack1l1llll1l_opy_ (u"ࠧࡴࡪࡲࡻࡎࡕࡓࡍࡱࡪ়ࠫ"),
  bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡲࡩࡑࡥࡺࡕࡷࡶࡦࡺࡥࡨࡻࠪঽ"),
  bstack1l1llll1l_opy_ (u"ࠩࡺࡩࡧࡱࡩࡵࡔࡨࡷࡵࡵ࡮ࡴࡧࡗ࡭ࡲ࡫࡯ࡶࡶࠪা"), bstack1l1llll1l_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡗࡢ࡫ࡷࡘ࡮ࡳࡥࡰࡷࡷࠫি"),
  bstack1l1llll1l_opy_ (u"ࠫࡷ࡫࡭ࡰࡶࡨࡈࡪࡨࡵࡨࡒࡵࡳࡽࡿࠧী"),
  bstack1l1llll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡆࡹࡹ࡯ࡥࡈࡼࡪࡩࡵࡵࡧࡉࡶࡴࡳࡈࡵࡶࡳࡷࠬু"),
  bstack1l1llll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡐࡴ࡭ࡃࡢࡲࡷࡹࡷ࡫ࠧূ"),
  bstack1l1llll1l_opy_ (u"ࠧࡸࡧࡥ࡯࡮ࡺࡄࡦࡤࡸ࡫ࡕࡸ࡯ࡹࡻࡓࡳࡷࡺࠧৃ"),
  bstack1l1llll1l_opy_ (u"ࠨࡨࡸࡰࡱࡉ࡯࡯ࡶࡨࡼࡹࡒࡩࡴࡶࠪৄ"),
  bstack1l1llll1l_opy_ (u"ࠩࡺࡥ࡮ࡺࡆࡰࡴࡄࡴࡵ࡙ࡣࡳ࡫ࡳࡸࠬ৅"),
  bstack1l1llll1l_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࡇࡴࡴ࡮ࡦࡥࡷࡖࡪࡺࡲࡪࡧࡶࠫ৆"),
  bstack1l1llll1l_opy_ (u"ࠫࡦࡶࡰࡏࡣࡰࡩࠬে"),
  bstack1l1llll1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡘ࡙ࡌࡄࡧࡵࡸࠬৈ"),
  bstack1l1llll1l_opy_ (u"࠭ࡴࡢࡲ࡚࡭ࡹ࡮ࡓࡩࡱࡵࡸࡕࡸࡥࡴࡵࡇࡹࡷࡧࡴࡪࡱࡱࠫ৉"),
  bstack1l1llll1l_opy_ (u"ࠧࡴࡥࡤࡰࡪࡌࡡࡤࡶࡲࡶࠬ৊"),
  bstack1l1llll1l_opy_ (u"ࠨࡹࡧࡥࡑࡵࡣࡢ࡮ࡓࡳࡷࡺࠧো"),
  bstack1l1llll1l_opy_ (u"ࠩࡶ࡬ࡴࡽࡘࡤࡱࡧࡩࡑࡵࡧࠨৌ"),
  bstack1l1llll1l_opy_ (u"ࠪ࡭ࡴࡹࡉ࡯ࡵࡷࡥࡱࡲࡐࡢࡷࡶࡩ্ࠬ"),
  bstack1l1llll1l_opy_ (u"ࠫࡽࡩ࡯ࡥࡧࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪ࠭ৎ"),
  bstack1l1llll1l_opy_ (u"ࠬࡱࡥࡺࡥ࡫ࡥ࡮ࡴࡐࡢࡵࡶࡻࡴࡸࡤࠨ৏"),
  bstack1l1llll1l_opy_ (u"࠭ࡵࡴࡧࡓࡶࡪࡨࡵࡪ࡮ࡷ࡛ࡉࡇࠧ৐"),
  bstack1l1llll1l_opy_ (u"ࠧࡱࡴࡨࡺࡪࡴࡴࡘࡆࡄࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠨ৑"),
  bstack1l1llll1l_opy_ (u"ࠨࡹࡨࡦࡉࡸࡩࡷࡧࡵࡅ࡬࡫࡮ࡵࡗࡵࡰࠬ৒"),
  bstack1l1llll1l_opy_ (u"ࠩ࡮ࡩࡾࡩࡨࡢ࡫ࡱࡔࡦࡺࡨࠨ৓"),
  bstack1l1llll1l_opy_ (u"ࠪࡹࡸ࡫ࡎࡦࡹ࡚ࡈࡆ࠭৔"),
  bstack1l1llll1l_opy_ (u"ࠫࡼࡪࡡࡍࡣࡸࡲࡨ࡮ࡔࡪ࡯ࡨࡳࡺࡺࠧ৕"), bstack1l1llll1l_opy_ (u"ࠬࡽࡤࡢࡅࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲ࡙࡯࡭ࡦࡱࡸࡸࠬ৖"),
  bstack1l1llll1l_opy_ (u"࠭ࡸࡤࡱࡧࡩࡔࡸࡧࡊࡦࠪৗ"), bstack1l1llll1l_opy_ (u"ࠧࡹࡥࡲࡨࡪ࡙ࡩࡨࡰ࡬ࡲ࡬ࡏࡤࠨ৘"),
  bstack1l1llll1l_opy_ (u"ࠨࡷࡳࡨࡦࡺࡥࡥ࡙ࡇࡅࡇࡻ࡮ࡥ࡮ࡨࡍࡩ࠭৙"),
  bstack1l1llll1l_opy_ (u"ࠩࡵࡩࡸ࡫ࡴࡐࡰࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡸࡴࡐࡰ࡯ࡽࠬ৚"),
  bstack1l1llll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡘ࡮ࡳࡥࡰࡷࡷࡷࠬ৛"),
  bstack1l1llll1l_opy_ (u"ࠫࡼࡪࡡࡔࡶࡤࡶࡹࡻࡰࡓࡧࡷࡶ࡮࡫ࡳࠨড়"), bstack1l1llll1l_opy_ (u"ࠬࡽࡤࡢࡕࡷࡥࡷࡺࡵࡱࡔࡨࡸࡷࡿࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠨঢ়"),
  bstack1l1llll1l_opy_ (u"࠭ࡣࡰࡰࡱࡩࡨࡺࡈࡢࡴࡧࡻࡦࡸࡥࡌࡧࡼࡦࡴࡧࡲࡥࠩ৞"),
  bstack1l1llll1l_opy_ (u"ࠧ࡮ࡣࡻࡘࡾࡶࡩ࡯ࡩࡉࡶࡪࡷࡵࡦࡰࡦࡽࠬয়"),
  bstack1l1llll1l_opy_ (u"ࠨࡵ࡬ࡱࡵࡲࡥࡊࡵ࡙࡭ࡸ࡯ࡢ࡭ࡧࡆ࡬ࡪࡩ࡫ࠨৠ"),
  bstack1l1llll1l_opy_ (u"ࠩࡸࡷࡪࡉࡡࡳࡶ࡫ࡥ࡬࡫ࡓࡴ࡮ࠪৡ"),
  bstack1l1llll1l_opy_ (u"ࠪࡷ࡭ࡵࡵ࡭ࡦࡘࡷࡪ࡙ࡩ࡯ࡩ࡯ࡩࡹࡵ࡮ࡕࡧࡶࡸࡒࡧ࡮ࡢࡩࡨࡶࠬৢ"),
  bstack1l1llll1l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡌ࡛ࡉࡖࠧৣ"),
  bstack1l1llll1l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡘࡴࡻࡣࡩࡋࡧࡉࡳࡸ࡯࡭࡮ࠪ৤"),
  bstack1l1llll1l_opy_ (u"࠭ࡩࡨࡰࡲࡶࡪࡎࡩࡥࡦࡨࡲࡆࡶࡩࡑࡱ࡯࡭ࡨࡿࡅࡳࡴࡲࡶࠬ৥"),
  bstack1l1llll1l_opy_ (u"ࠧ࡮ࡱࡦ࡯ࡑࡵࡣࡢࡶ࡬ࡳࡳࡇࡰࡱࠩ০"),
  bstack1l1llll1l_opy_ (u"ࠨ࡮ࡲ࡫ࡨࡧࡴࡇࡱࡵࡱࡦࡺࠧ১"), bstack1l1llll1l_opy_ (u"ࠩ࡯ࡳ࡬ࡩࡡࡵࡈ࡬ࡰࡹ࡫ࡲࡔࡲࡨࡧࡸ࠭২"),
  bstack1l1llll1l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡆࡨࡰࡦࡿࡁࡥࡤࠪ৩")
]
bstack1ll1l11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡹࡵࡲ࡯ࡢࡦࠪ৪")
bstack11l11ll1_opy_ = [bstack1l1llll1l_opy_ (u"ࠬ࠴ࡡࡱ࡭ࠪ৫"), bstack1l1llll1l_opy_ (u"࠭࠮ࡢࡣࡥࠫ৬"), bstack1l1llll1l_opy_ (u"ࠧ࠯࡫ࡳࡥࠬ৭")]
bstack11lllll1l_opy_ = [bstack1l1llll1l_opy_ (u"ࠨ࡫ࡧࠫ৮"), bstack1l1llll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ৯"), bstack1l1llll1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ৰ"), bstack1l1llll1l_opy_ (u"ࠫࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦࠪৱ")]
bstack111ll1_opy_ = {
  bstack1l1llll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ৲"): bstack1l1llll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ৳"),
  bstack1l1llll1l_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨ৴"): bstack1l1llll1l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭৵"),
  bstack1l1llll1l_opy_ (u"ࠩࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ৶"): bstack1l1llll1l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ৷"),
  bstack1l1llll1l_opy_ (u"ࠫ࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ৸"): bstack1l1llll1l_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ৹"),
  bstack1l1llll1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮ࡕࡰࡵ࡫ࡲࡲࡸ࠭৺"): bstack1l1llll1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ৻")
}
bstack11l11111l_opy_ = [
  bstack1l1llll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ৼ"),
  bstack1l1llll1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ৽"),
  bstack1l1llll1l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ৾"),
  bstack1l1llll1l_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ৿"),
  bstack1l1llll1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭਀"),
]
bstack1l11l11ll_opy_ = bstack11ll1ll1l_opy_ + bstack1l111l_opy_ + bstack111l1_opy_
bstack1l1111_opy_ = [
  bstack1l1llll1l_opy_ (u"࠭࡞࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶࠧࠫਁ"),
  bstack1l1llll1l_opy_ (u"ࠧ࡟ࡤࡶ࠱ࡱࡵࡣࡢ࡮࠱ࡧࡴࡳࠤࠨਂ"),
  bstack1l1llll1l_opy_ (u"ࠨࡠ࠴࠶࠼࠴ࠧਃ"),
  bstack1l1llll1l_opy_ (u"ࠩࡡ࠵࠵࠴ࠧ਄"),
  bstack1l1llll1l_opy_ (u"ࠪࡢ࠶࠽࠲࠯࠳࡞࠺࠲࠿࡝࠯ࠩਅ"),
  bstack1l1llll1l_opy_ (u"ࠫࡣ࠷࠷࠳࠰࠵࡟࠵࠳࠹࡞࠰ࠪਆ"),
  bstack1l1llll1l_opy_ (u"ࠬࡤ࠱࠸࠴࠱࠷ࡠ࠶࠭࠲࡟࠱ࠫਇ"),
  bstack1l1llll1l_opy_ (u"࠭࡞࠲࠻࠵࠲࠶࠼࠸࠯ࠩਈ")
]
bstack1llll1l_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀࠫਉ")
bstack1ll111ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡵࡧ࡯࠴ࡼ࠱࠰ࡧࡹࡩࡳࡺࠧਊ")
bstack111111l1_opy_ = [ bstack1l1llll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ਋") ]
bstack1ll1l11l_opy_ = [ bstack1l1llll1l_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩ਌") ]
bstack111lll1l1_opy_ = [ bstack1l1llll1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ਍") ]
bstack111lll11_opy_ = bstack1l1llll1l_opy_ (u"࡙ࠬࡄࡌࡕࡨࡸࡺࡶࠧ਎")
bstack11l1l11l_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡓࡅࡍࡗࡩࡸࡺࡁࡵࡶࡨࡱࡵࡺࡥࡥࠩਏ")
bstack111ll111l_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡔࡆࡎࡘࡪࡹࡴࡔࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠫਐ")
bstack11l_opy_ = bstack1l1llll1l_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࠧ਑")
bstack11ll1l1_opy_ = [
  bstack1l1llll1l_opy_ (u"ࠩࡈࡖࡗࡥࡆࡂࡋࡏࡉࡉ࠭਒"),
  bstack1l1llll1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡕࡋࡐࡉࡉࡥࡏࡖࡖࠪਓ"),
  bstack1l1llll1l_opy_ (u"ࠫࡊࡘࡒࡠࡄࡏࡓࡈࡑࡅࡅࡡࡅ࡝ࡤࡉࡌࡊࡇࡑࡘࠬਔ"),
  bstack1l1llll1l_opy_ (u"ࠬࡋࡒࡓࡡࡑࡉ࡙࡝ࡏࡓࡍࡢࡇࡍࡇࡎࡈࡇࡇࠫਕ"),
  bstack1l1llll1l_opy_ (u"࠭ࡅࡓࡔࡢࡗࡔࡉࡋࡆࡖࡢࡒࡔ࡚࡟ࡄࡑࡑࡒࡊࡉࡔࡆࡆࠪਖ"),
  bstack1l1llll1l_opy_ (u"ࠧࡆࡔࡕࡣࡈࡕࡎࡏࡇࡆࡘࡎࡕࡎࡠࡅࡏࡓࡘࡋࡄࠨਗ"),
  bstack1l1llll1l_opy_ (u"ࠨࡇࡕࡖࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡕࡉࡘࡋࡔࠨਘ"),
  bstack1l1llll1l_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡖࡊࡌࡕࡔࡇࡇࠫਙ"),
  bstack1l1llll1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡆࡈࡏࡓࡖࡈࡈࠬਚ"),
  bstack1l1llll1l_opy_ (u"ࠫࡊࡘࡒࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬਛ"),
  bstack1l1llll1l_opy_ (u"ࠬࡋࡒࡓࡡࡑࡅࡒࡋ࡟ࡏࡑࡗࡣࡗࡋࡓࡐࡎ࡙ࡉࡉ࠭ਜ"),
  bstack1l1llll1l_opy_ (u"࠭ࡅࡓࡔࡢࡅࡉࡊࡒࡆࡕࡖࡣࡎࡔࡖࡂࡎࡌࡈࠬਝ"),
  bstack1l1llll1l_opy_ (u"ࠧࡆࡔࡕࡣࡆࡊࡄࡓࡇࡖࡗࡤ࡛ࡎࡓࡇࡄࡇࡍࡇࡂࡍࡇࠪਞ"),
  bstack1l1llll1l_opy_ (u"ࠨࡇࡕࡖࡤ࡚ࡕࡏࡐࡈࡐࡤࡉࡏࡏࡐࡈࡇ࡙ࡏࡏࡏࡡࡉࡅࡎࡒࡅࡅࠩਟ"),
  bstack1l1llll1l_opy_ (u"ࠩࡈࡖࡗࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡘࡎࡓࡅࡅࡡࡒ࡙࡙࠭ਠ"),
  bstack1l1llll1l_opy_ (u"ࠪࡉࡗࡘ࡟ࡔࡑࡆࡏࡘࡥࡃࡐࡐࡑࡉࡈ࡚ࡉࡐࡐࡢࡊࡆࡏࡌࡆࡆࠪਡ"),
  bstack1l1llll1l_opy_ (u"ࠫࡊࡘࡒࡠࡕࡒࡇࡐ࡙࡟ࡄࡑࡑࡒࡊࡉࡔࡊࡑࡑࡣࡍࡕࡓࡕࡡࡘࡒࡗࡋࡁࡄࡊࡄࡆࡑࡋࠧਢ"),
  bstack1l1llll1l_opy_ (u"ࠬࡋࡒࡓࡡࡓࡖࡔ࡞࡙ࡠࡅࡒࡒࡓࡋࡃࡕࡋࡒࡒࡤࡌࡁࡊࡎࡈࡈࠬਣ"),
  bstack1l1llll1l_opy_ (u"࠭ࡅࡓࡔࡢࡒࡆࡓࡅࡠࡐࡒࡘࡤࡘࡅࡔࡑࡏ࡚ࡊࡊࠧਤ"),
  bstack1l1llll1l_opy_ (u"ࠧࡆࡔࡕࡣࡓࡇࡍࡆࡡࡕࡉࡘࡕࡌࡖࡖࡌࡓࡓࡥࡆࡂࡋࡏࡉࡉ࠭ਥ"),
  bstack1l1llll1l_opy_ (u"ࠨࡇࡕࡖࡤࡓࡁࡏࡆࡄࡘࡔࡘ࡙ࡠࡒࡕࡓ࡝࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟ࡇࡃࡌࡐࡊࡊࠧਦ"),
]
bstack11l1ll1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠩ࠱࠳ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡥࡷࡺࡩࡧࡣࡦࡸࡸ࠵ࠧਧ")
def bstack1l11ll111_opy_():
  global CONFIG
  headers = {
        bstack1l1llll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਨ"): bstack1l1llll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ਩"),
      }
  proxies = bstack1_opy_(CONFIG, bstack1ll11l1l_opy_)
  try:
    response = requests.get(bstack1ll11l1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1lll1l1ll_opy_ = response.json()[bstack1l1llll1l_opy_ (u"ࠬ࡮ࡵࡣࡵࠪਪ")]
      logger.debug(bstack1l1lll1_opy_.format(response.json()))
      return bstack1lll1l1ll_opy_
    else:
      logger.debug(bstack11l111ll1_opy_.format(bstack1l1llll1l_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਫ")))
  except Exception as e:
    logger.debug(bstack11l111ll1_opy_.format(e))
def bstack11l1111l_opy_(hub_url):
  global CONFIG
  url = bstack1l1llll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਬ")+  hub_url + bstack1l1llll1l_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣਭ")
  headers = {
        bstack1l1llll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਮ"): bstack1l1llll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਯ"),
      }
  proxies = bstack1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l11llll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1lllll1_opy_.format(hub_url, e))
def bstack1111l11_opy_():
  try:
    global bstack1ll1lll_opy_
    bstack1lll1l1ll_opy_ = bstack1l11ll111_opy_()
    bstack11l1lll1l_opy_ = []
    results = []
    for bstack11lll1l1l_opy_ in bstack1lll1l1ll_opy_:
      bstack11l1lll1l_opy_.append(bstack1l11ll_opy_(target=bstack11l1111l_opy_,args=(bstack11lll1l1l_opy_,)))
    for t in bstack11l1lll1l_opy_:
      t.start()
    for t in bstack11l1lll1l_opy_:
      results.append(t.join())
    bstack1ll1lll11_opy_ = {}
    for item in results:
      hub_url = item[bstack1l1llll1l_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬਰ")]
      latency = item[bstack1l1llll1l_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭਱")]
      bstack1ll1lll11_opy_[hub_url] = latency
    bstack1ll1111_opy_ = min(bstack1ll1lll11_opy_, key= lambda x: bstack1ll1lll11_opy_[x])
    bstack1ll1lll_opy_ = bstack1ll1111_opy_
    logger.debug(bstack1l1111ll_opy_.format(bstack1ll1111_opy_))
  except Exception as e:
    logger.debug(bstack1l1llll11_opy_.format(e))
bstack1lll1ll11_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡓࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡲࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠼ࠣࡿࢂ࠭ਲ")
bstack111l1l1l_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡄࡱࡰࡴࡱ࡫ࡴࡦࡦࠣࡷࡪࡺࡵࡱࠣࠪਲ਼")
bstack11l1l11ll_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡒࡤࡶࡸ࡫ࡤࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪ਴")
bstack1l11ll11_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡖࡥࡳ࡯ࡴࡪࡼࡨࡨࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧਵ")
bstack11lll1ll1_opy_ = bstack1l1llll1l_opy_ (u"࡙ࠪࡸ࡯࡮ࡨࠢ࡫ࡹࡧࠦࡵࡳ࡮࠽ࠤࢀࢃࠧਸ਼")
bstack111llll11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡘ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࡽࢀࠫ਷")
bstack111l1l1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡘࡥࡤࡧ࡬ࡺࡪࡪࠠࡪࡰࡷࡩࡷࡸࡵࡱࡶ࠯ࠤࡪࡾࡩࡵ࡫ࡱ࡫ࠬਸ")
bstack11lllll_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳ࠯ࠢࡣࡴ࡮ࡶࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡵࡨࡰࡪࡴࡩࡶ࡯ࡣࠫਹ")
bstack11111111_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴࠡࡣࡱࡨࠥࡶࡹࡵࡧࡶࡸ࠲ࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡱࡣࡦ࡯ࡦ࡭ࡥࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡶࡩࡱ࡫࡮ࡪࡷࡰࡤࠬ਺")
bstack1ll11ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡄࡴࡵ࡯ࡵ࡮ࡎ࡬ࡦࡷࡧࡲࡺࠢࡳࡥࡨࡱࡡࡨࡧ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠱ࡦࡶࡰࡪࡷࡰࡰ࡮ࡨࡲࡢࡴࡼࡤࠬ਻")
bstack1ll11l1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡶࡴࡨ࡯ࡵ࠮ࠣࡴࡦࡨ࡯ࡵࠢࡤࡲࡩࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࡭࡫ࡥࡶࡦࡸࡹࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡸࡴࠦࡲࡶࡰࠣࡶࡴࡨ࡯ࡵࠢࡷࡩࡸࡺࡳࠡ࡫ࡱࠤࡵࡧࡲࡢ࡮࡯ࡩࡱ࠴ࠠࡡࡲ࡬ࡴࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡲࡰࡤࡲࡸ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠮ࡲࡤࡦࡴࡺࠠࡳࡱࡥࡳࡹ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠮ࡵࡨࡰࡪࡴࡩࡶ࡯࡯࡭ࡧࡸࡡࡳࡻࡣ਼ࠫ")
bstack1l11l111_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵ࠱ࠤࡥࡶࡩࡱࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡦࡪ࡮ࡡࡷࡧࡣࠫ਽")
bstack1l111l11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡧࡰࡱ࡫ࡸࡱ࠲ࡩ࡬ࡪࡧࡱࡸࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶ࠲ࠥࡦࡰࡪࡲࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡆࡶࡰࡪࡷࡰ࠱ࡕࡿࡴࡩࡱࡱ࠱ࡈࡲࡩࡦࡰࡷࡤࠬਾ")
bstack11l1l1111_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡸࡴࠦࡲࡶࡰࠣࡸࡪࡹࡴࡴ࠰ࠣࡤࡵ࡯ࡰࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡦࠧਿ")
bstack111lll11l_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡃࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡩ࡭ࡳࡪࠠࡦ࡫ࡷ࡬ࡪࡸࠠࡔࡧ࡯ࡩࡳ࡯ࡵ࡮ࠢࡲࡶࠥࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳ࠯ࠢࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡹࡧ࡬࡭ࠢࡷ࡬ࡪࠦࡲࡦ࡮ࡨࡺࡦࡴࡴࠡࡲࡤࡧࡰࡧࡧࡦࡵࠣࡹࡸ࡯࡮ࡨࠢࡳ࡭ࡵࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷ࠳࠭ੀ")
bstack1llll1_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡉࡣࡱࡨࡱ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡱࡵࡳࡦࠩੁ")
bstack111lll_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡃ࡯ࡰࠥࡪ࡯࡯ࡧࠤࠫੂ")
bstack1111llll1_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡆࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴࠡࡣࡷࠤࡦࡴࡹࠡࡲࡤࡶࡪࡴࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡴ࡬ࠠࠣࡽࢀࠦ࠳ࠦࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡥ࡯ࡹࡩ࡫ࠠࡢࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰ࠴ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠢࡩ࡭ࡱ࡫ࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࡹ࠮ࠨ੃")
bstack111l11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡶࡪࡪࡥ࡯ࡶ࡬ࡥࡱࡹࠠ࡯ࡱࡷࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡢࡦࡧࠤࡹ࡮ࡥ࡮ࠢ࡬ࡲࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࠦࡡࡴࠢࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧࠦࡡ࡯ࡦࠣࠦࡦࡩࡣࡦࡵࡶࡏࡪࡿࠢࠡࡱࡵࠤࡸ࡫ࡴࠡࡶ࡫ࡩࡲࠦࡡࡴࠢࡨࡲࡻ࡯ࡲࡰࡰࡰࡩࡳࡺࠠࡷࡣࡵ࡭ࡦࡨ࡬ࡦࡵ࠽ࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨࠠࡢࡰࡧࠤࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠣࠩ੄")
bstack1llll_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡒࡧ࡬ࡧࡱࡵࡱࡪࡪࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠿ࠨࡻࡾࠤࠪ੅")
bstack111llll1_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡋ࡮ࡤࡱࡸࡲࡹ࡫ࡲࡦࡦࠣࡩࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡸࡴࠥ࠳ࠠࡼࡿࠪ੆")
bstack1ll11111_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱ࠭ੇ")
bstack1ll11l_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡎࡲࡧࡦࡲࠧੈ")
bstack1lll1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡍࡱࡦࡥࡱࠦࡩࡴࠢࡱࡳࡼࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠡࠨ੉")
bstack111111ll_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࠤࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡐࡴࡩࡡ࡭࠼ࠣࡿࢂ࠭੊")
bstack1l1ll1l1l_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡼ࡯ࡴࡩࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࢀࢃࠧੋ")
bstack1l1ll111l_opy_ = bstack1l1llll1l_opy_ (u"࡚ࠫࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡥࡧࡷࡥ࡮ࡲࡳ࠻ࠢࡾࢁࠬੌ")
bstack1ll11ll1l_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡷࡳࡨࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀ੍ࠫ")
bstack1l11lll_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࠠࡢࡰࠣࡥࡵࡶࡲࡰࡲࡵ࡭ࡦࡺࡥࠡࡈ࡚ࠤ࠭ࡸ࡯ࡣࡱࡷ࠳ࡵࡧࡢࡰࡶࠬࠤ࡮ࡴࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠱ࠦࡳ࡬࡫ࡳࠤࡹ࡮ࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤࡰ࡫ࡹࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࡮࡬ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡵ࡬ࡱࡵࡲࡥࠡࡲࡼࡸ࡭ࡵ࡮ࠡࡵࡦࡶ࡮ࡶࡴࠡࡹ࡬ࡸ࡭ࡵࡵࡵࠢࡤࡲࡾࠦࡆࡘ࠰ࠪ੎")
bstack11ll1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡔࡧࡷࡸ࡮ࡴࡧࠡࡪࡷࡸࡵࡖࡲࡰࡺࡼ࠳࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡴࡴࠠࡤࡷࡵࡶࡪࡴࡴ࡭ࡻࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡰࡨࠣࡷࡪࡲࡥ࡯࡫ࡸࡱࠥ࠮ࡻࡾࠫ࠯ࠤࡵࡲࡥࡢࡵࡨࠤࡺࡶࡧࡳࡣࡧࡩࠥࡺ࡯ࠡࡕࡨࡰࡪࡴࡩࡶ࡯ࡁࡁ࠹࠴࠰࠯࠲ࠣࡳࡷࠦࡲࡦࡨࡨࡶࠥࡺ࡯ࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡱ࡫࡮ࡪࡷࡰ࠳ࡷࡻ࡮࠮ࡶࡨࡷࡹࡹ࠭ࡣࡧ࡫࡭ࡳࡪ࠭ࡱࡴࡲࡼࡾࠩࡰࡺࡶ࡫ࡳࡳࠦࡦࡰࡴࠣࡥࠥࡽ࡯ࡳ࡭ࡤࡶࡴࡻ࡮ࡥ࠰ࠪ੏")
bstack1ll1ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴࠮ࠨ੐")
bstack1l1l1lll1_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡩࡨࡲࡪࡸࡡࡵࡧࡧࠤࡹ࡮ࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠧࠧੑ")
bstack1ll1ll111_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡶ࡫ࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫࡯࡬ࡦ࠰ࠣࡿࢂ࠭੒")
bstack111lll1_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡊࡾࡰࡦࡥࡷࡩࡩࠦࡡࡵࠢ࡯ࡩࡦࡹࡴࠡ࠳ࠣ࡭ࡳࡶࡵࡵ࠮ࠣࡶࡪࡩࡥࡪࡸࡨࡨࠥ࠶ࠧ੓")
bstack11l1l1l_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡩࡻࡲࡪࡰࡪࠤࡆࡶࡰࠡࡷࡳࡰࡴࡧࡤ࠯ࠢࡾࢁࠬ੔")
bstack1l1l11l1l_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡸࡴࡱࡵࡡࡥࠢࡄࡴࡵ࠴ࠠࡊࡰࡹࡥࡱ࡯ࡤࠡࡨ࡬ࡰࡪࠦࡰࡢࡶ࡫ࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡻࡾ࠰ࠪ੕")
bstack1llllllll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡌࡧࡼࡷࠥࡩࡡ࡯ࡰࡲࡸࠥࡩ࡯࠮ࡧࡻ࡭ࡸࡺࠠࡢࡵࠣࡥࡵࡶࠠࡷࡣ࡯ࡹࡪࡹࠬࠡࡷࡶࡩࠥࡧ࡮ࡺࠢࡲࡲࡪࠦࡰࡳࡱࡳࡩࡷࡺࡹࠡࡨࡵࡳࡲࠦࡻࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡶࡡࡵࡪ࠿ࡷࡹࡸࡩ࡯ࡩࡁ࠰ࠥࡩࡵࡴࡶࡲࡱࡤ࡯ࡤ࠽ࡵࡷࡶ࡮ࡴࡧ࠿࠮ࠣࡷ࡭ࡧࡲࡦࡣࡥࡰࡪࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀࢀ࠰ࠥࡵ࡮࡭ࡻࠣࠦࡵࡧࡴࡩࠤࠣࡥࡳࡪࠠࠣࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠦࠥࡩࡡ࡯ࠢࡦࡳ࠲࡫ࡸࡪࡵࡷࠤࡹࡵࡧࡦࡶ࡫ࡩࡷ࠴ࠧ੖")
bstack1llllll_opy_ = bstack1l1llll1l_opy_ (u"ࠨ࡝ࡌࡲࡻࡧ࡬ࡪࡦࠣࡥࡵࡶࠠࡱࡴࡲࡴࡪࡸࡴࡺ࡟ࠣࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠣࡥࡷ࡫ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪ੗")
bstack11l1l11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠩ࡞ࡍࡳࡼࡡ࡭࡫ࡧࠤࡦࡶࡰࠡࡲࡵࡳࡵ࡫ࡲࡵࡻࡠࠤࡘࡻࡰࡱࡱࡵࡸࡪࡪࠠࡷࡣ࡯ࡹࡪࡹࠠࡰࡨࠣࡥࡵࡶࠠࡢࡴࡨࠤࡴ࡬ࠠࡼ࡫ࡧࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡰࡢࡶ࡫ࡀࡸࡺࡲࡪࡰࡪࡂ࠱ࠦࡣࡶࡵࡷࡳࡲࡥࡩࡥ࠾ࡶࡸࡷ࡯࡮ࡨࡀ࠯ࠤࡸ࡮ࡡࡳࡧࡤࡦࡱ࡫࡟ࡪࡦ࠿ࡷࡹࡸࡩ࡯ࡩࡁࢁ࠳ࠦࡆࡰࡴࠣࡱࡴࡸࡥࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡳࡰࡪࡧࡳࡦࠢࡹ࡭ࡸ࡯ࡴࠡࡪࡷࡸࡵࡹ࠺࠰࠱ࡺࡻࡼ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡧࡳࡨࡹ࠯ࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡡࡱࡲ࡬ࡹࡲ࠵ࡳࡦࡶ࠰ࡹࡵ࠳ࡴࡦࡵࡷࡷ࠴ࡹࡰࡦࡥ࡬ࡪࡾ࠳ࡡࡱࡲࠪ੘")
bstack1l11l1ll1_opy_ = bstack1l1llll1l_opy_ (u"࡙ࠪࡸ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡦࡶࡰࠡ࡫ࡧࠤࢀࢃࠠࡧࡱࡵࠤ࡭ࡧࡳࡩࠢ࠽ࠤࢀࢃ࠮ࠨਖ਼")
bstack1111lllll_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡆࡶࡰࠡࡗࡳࡰࡴࡧࡤࡦࡦࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺ࠰ࠣࡍࡉࠦ࠺ࠡࡽࢀࠫਗ਼")
bstack11ll111l1_opy_ = bstack1l1llll1l_opy_ (u"࡛ࠬࡳࡪࡰࡪࠤࡆࡶࡰࠡ࠼ࠣࡿࢂ࠴ࠧਜ਼")
bstack1lll11ll_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲࠦࡩࡴࠢࡱࡳࡹࠦࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡩࡳࡷࠦࡶࡢࡰ࡬ࡰࡱࡧࠠࡱࡻࡷ࡬ࡴࡴࠠࡵࡧࡶࡸࡸ࠲ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡰࡢࡴࡤࡰࡱ࡫࡬ࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠥࡃࠠ࠲ࠩੜ")
bstack1l1ll1lll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࡀࠠࡼࡿࠪ੝")
bstack1lll11ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡅࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡨࡲ࡯ࡴࡧࠣࡦࡷࡵࡷࡴࡧࡵ࠾ࠥࢁࡽࠨਫ਼")
bstack1l1l_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡆࡳࡺࡲࡤࠡࡰࡲࡸࠥ࡭ࡥࡵࠢࡵࡩࡦࡹ࡯࡯ࠢࡩࡳࡷࠦࡢࡦࡪࡤࡺࡪࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥ࠯ࠢࡾࢁࠬ੟")
bstack11l1ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡤࡴ࡮ࠦࡣࡢ࡮࡯࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ੠")
bstack1111111l_opy_ = bstack1l1llll1l_opy_ (u"࡚ࠫࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡪࡲࡻࠥࡨࡵࡪ࡮ࡧࠤ࡚ࡘࡌ࠭ࠢࡤࡷࠥࡨࡵࡪ࡮ࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠡ࡫ࡶࠤࡳࡵࡴࠡࡷࡶࡩࡩ࠴ࠧ੡")
bstack1ll11l1ll_opy_ = bstack1l1llll1l_opy_ (u"࡙ࠬࡥࡳࡸࡨࡶࠥࡹࡩࡥࡧࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠮ࡻࡾࠫࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡦࡳࡥࠡࡣࡶࠤࡨࡲࡩࡦࡰࡷࠤࡸ࡯ࡤࡦࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩ࠭ࢁࡽࠪࠩ੢")
bstack111l1l11_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡖࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡳࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡪࡡࡴࡪࡥࡳࡦࡸࡤ࠻ࠢࡾࢁࠬ੣")
bstack1l1l111l_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡥࡨࡩࡥࡴࡵࠣࡥࠥࡶࡲࡪࡸࡤࡸࡪࠦࡤࡰ࡯ࡤ࡭ࡳࡀࠠࡼࡿࠣ࠲࡙ࠥࡥࡵࠢࡷ࡬ࡪࠦࡦࡰ࡮࡯ࡳࡼ࡯࡮ࡨࠢࡦࡳࡳ࡬ࡩࡨࠢ࡬ࡲࠥࡿ࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱࠦࡦࡪ࡮ࡨ࠾ࠥࡢ࡮࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠥࡢ࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰ࠿ࠦࡴࡳࡷࡨࠤࡡࡴ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠫ੤")
bstack111_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡕࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡦࡺࡨࡧࡺࡺࡩ࡯ࡩࠣ࡫ࡪࡺ࡟࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࡤ࡫ࡲࡳࡱࡵࠤ࠿ࠦࡻࡾࠩ੥")
bstack11ll11l11_opy_ = bstack1l1llll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫࡮ࡥࡡࡤࡱࡵࡲࡩࡵࡷࡧࡩࡤ࡫ࡶࡦࡰࡷࠤ࡫ࡵࡲࠡࡕࡇࡏࡘ࡫ࡴࡶࡲࠣࡿࢂࠨ੦")
bstack1l11llll1_opy_ = bstack1l1llll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥ࡯ࡦࡢࡥࡲࡶ࡬ࡪࡶࡸࡨࡪࡥࡥࡷࡧࡱࡸࠥ࡬࡯ࡳࠢࡖࡈࡐ࡚ࡥࡴࡶࡄࡸࡹ࡫࡭ࡱࡶࡨࡨࠥࢁࡽࠣ੧")
bstack11l11_opy_ = bstack1l1llll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡰࡧࡣࡦࡳࡰ࡭࡫ࡷࡹࡩ࡫࡟ࡦࡸࡨࡲࡹࠦࡦࡰࡴࠣࡗࡉࡑࡔࡦࡵࡷࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠠࡼࡿࠥ੨")
bstack1lll1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡵࡩࡤࡸࡥࡲࡷࡨࡷࡹࠦࡻࡾࠤ੩")
bstack1l111lll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡐࡐࡕࡗࠤࡊࡼࡥ࡯ࡶࠣࡿࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡ࠼ࠣࡿࢂࠨ੪")
bstack1l1l1l1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࠦࡰࡳࡱࡻࡽࠥࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠫ੫")
bstack1l1lll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡ࠱ࡱࡩࡽࡺ࡟ࡩࡷࡥࡷࠥࢁࡽࠨ੬")
bstack11l111ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡧࡴࡲࡱࠥ࠵࡮ࡦࡺࡷࡣ࡭ࡻࡢࡴ࠼ࠣࡿࢂ࠭੭")
bstack1l1111ll_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡒࡪࡧࡲࡦࡵࡷࠤ࡭ࡻࡢࠡࡣ࡯ࡰࡴࡩࡡࡵࡧࡧࠤ࡮ࡹ࠺ࠡࡽࢀࠫ੮")
bstack1l1llll11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡊࡘࡒࡐࡔࠣࡍࡓࠦࡁࡍࡎࡒࡇࡆ࡚ࡅࠡࡊࡘࡆࠥࢁࡽࠨ੯")
bstack1l11llll_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡒࡡࡵࡧࡱࡧࡾࠦ࡯ࡧࠢ࡫ࡹࡧࡀࠠࡼࡿࠣ࡭ࡸࡀࠠࡼࡿࠪੰ")
bstack1l1lllll1_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢ࡯ࡥࡹ࡫࡮ࡤࡻࠣࡪࡴࡸࠠࡼࡿࠣ࡬ࡺࡨ࠺ࠡࡽࢀࠫੱ")
bstack11l11ll11_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡉࡷࡥࠤࡺࡸ࡬ࠡࡥ࡫ࡥࡳ࡭ࡥࡥࠢࡷࡳࠥࡺࡨࡦࠢࡲࡴࡹ࡯࡭ࡢ࡮ࠣ࡬ࡺࡨ࠺ࠡࡽࢀࠫੲ")
bstack1l1lll11_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡴࡶࡴࡪ࡯ࡤࡰࠥ࡮ࡵࡣࠢࡸࡶࡱࡀࠠࡼࡿࠪੳ")
bstack11l1l_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡰ࡮ࡹࡴࡴ࠼ࠣࡿࢂ࠭ੴ")
bstack1l111ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴ࠼ࠣࡿࢂ࠭ੵ")
bstack11l11lll_opy_ = bstack1l1llll1l_opy_ (u"࡚ࠫࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡰࡢࡥࠣࡪ࡮ࡲࡥࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠩ੶")
bstack1ll1l111_opy_ = bstack1l1llll1l_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬ੷")
bstack11ll1l111_opy_ = bstack1l1llll1l_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬ੸")
from ._version import __version__
bstack11ll1l1l1_opy_ = None
CONFIG = {}
bstack1l11l11_opy_ = {}
bstack111l11111_opy_ = {}
bstack1ll11_opy_ = None
bstack1l1ll1ll_opy_ = None
bstack1ll1111l_opy_ = None
bstack1l1llll_opy_ = -1
bstack11l1l1ll1_opy_ = bstack1l11_opy_
bstack1l11111l1_opy_ = 1
bstack1ll1llll_opy_ = False
bstack1l1ll1111_opy_ = False
bstack1l1lll11l_opy_ = bstack1l1llll1l_opy_ (u"ࠧࠨ੹")
bstack11l1l111_opy_ = bstack1l1llll1l_opy_ (u"ࠨࠩ੺")
bstack111l1l111_opy_ = False
bstack11l11ll_opy_ = True
bstack11l1l1lll_opy_ = bstack1l1llll1l_opy_ (u"ࠩࠪ੻")
bstack1ll1l1ll_opy_ = []
bstack1ll1lll_opy_ = bstack1l1llll1l_opy_ (u"ࠪࠫ੼")
bstack1lll1l1_opy_ = False
bstack11l1l1l1l_opy_ = None
bstack1l1l1ll1_opy_ = None
bstack11l11l1l1_opy_ = -1
bstack11l1lllll_opy_ = os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠫࢃ࠭੽")), bstack1l1llll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ੾"), bstack1l1llll1l_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫ੿"))
bstack11ll1l11_opy_ = []
bstack1ll111l1l_opy_ = False
bstack111ll1l1_opy_ = False
bstack11ll1lll1_opy_ = None
bstack111l_opy_ = None
bstack1l1l11ll1_opy_ = None
bstack11ll1lll_opy_ = None
bstack1l1lll1l1_opy_ = None
bstack1l11l_opy_ = None
bstack1l1l111_opy_ = None
bstack11ll1l11l_opy_ = None
bstack11lll111l_opy_ = None
bstack1ll111l11_opy_ = None
bstack1lllll111_opy_ = None
bstack1l1ll11l1_opy_ = None
bstack1l11l1ll_opy_ = None
bstack11ll1ll11_opy_ = None
bstack1lll1111_opy_ = None
bstack11llll_opy_ = None
bstack1l11l111l_opy_ = None
bstack11l11ll1l_opy_ = None
bstack11ll1l1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠢࠣ઀")
class bstack1l11ll_opy_(threading.Thread):
  def run(self):
    self.exc = None
    try:
      self.ret = self._target(*self._args, **self._kwargs)
    except Exception as e:
      self.exc = e
  def join(self, timeout=None):
    super(bstack1l11ll_opy_, self).join(timeout)
    if self.exc:
      raise self.exc
    return self.ret
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11l1l1ll1_opy_,
                    format=bstack1l1llll1l_opy_ (u"ࠨ࡞ࡱࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ઁ"),
                    datefmt=bstack1l1llll1l_opy_ (u"ࠩࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫં"))
def bstack11l1111ll_opy_():
  global CONFIG
  global bstack11l1l1ll1_opy_
  if bstack1l1llll1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬઃ") in CONFIG:
    bstack11l1l1ll1_opy_ = bstack1llll11l_opy_[CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭઄")]]
    logging.getLogger().setLevel(bstack11l1l1ll1_opy_)
def bstack11lll11l_opy_():
  global CONFIG
  global bstack1ll111l1l_opy_
  bstack111ll11l1_opy_ = bstack1lll111l1_opy_(CONFIG)
  if(bstack1l1llll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧઅ") in bstack111ll11l1_opy_ and str(bstack111ll11l1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨઆ")]).lower() == bstack1l1llll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬઇ")):
    bstack1ll111l1l_opy_ = True
def bstack11l111111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11lll1111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l11l1lll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l1llll1l_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧઈ") == args[i].lower() or bstack1l1llll1l_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥઉ") == args[i].lower():
      path = args[i+1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l1l1lll_opy_
      bstack11l1l1lll_opy_ += bstack1l1llll1l_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨઊ") + path
      return path
  return None
bstack1111111_opy_ = re.compile(bstack1l1llll1l_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢઋ"))
def bstack1l111l1l1_opy_(loader, node):
    value = loader.construct_scalar(node)
    for group in bstack1111111_opy_.findall(value):
        if group is not None and os.environ.get(group) is not None:
          value = value.replace(bstack1l1llll1l_opy_ (u"ࠧࠪࡻࠣઌ") + group + bstack1l1llll1l_opy_ (u"ࠨࡽࠣઍ"), os.environ.get(group))
    return value
def bstack11ll11l_opy_():
  bstack1l111111l_opy_ = bstack1l11l1lll_opy_()
  if bstack1l111111l_opy_ and os.path.exists(os.path.abspath(bstack1l111111l_opy_)):
    fileName = bstack1l111111l_opy_
  if bstack1l1llll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ઎") in os.environ and os.path.exists(os.path.abspath(os.environ[bstack1l1llll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬએ")])) and not bstack1l1llll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫઐ") in locals():
    fileName = os.environ[bstack1l1llll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧઑ")]
  if bstack1l1llll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭઒") in locals():
    bstack1ll1111ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1ll1111ll_opy_ = bstack1l1llll1l_opy_ (u"ࠬ࠭ઓ")
  bstack11l111l1_opy_ = os.getcwd()
  bstack111llll_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩઔ")
  bstack11ll111_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫક")
  while (not os.path.exists(bstack1ll1111ll_opy_)) and bstack11l111l1_opy_ != bstack1l1llll1l_opy_ (u"ࠣࠤખ"):
    bstack1ll1111ll_opy_ = os.path.join(bstack11l111l1_opy_, bstack111llll_opy_)
    if not os.path.exists(bstack1ll1111ll_opy_):
      bstack1ll1111ll_opy_ = os.path.join(bstack11l111l1_opy_, bstack11ll111_opy_)
    if bstack11l111l1_opy_ != os.path.dirname(bstack11l111l1_opy_):
      bstack11l111l1_opy_ = os.path.dirname(bstack11l111l1_opy_)
    else:
      bstack11l111l1_opy_ = bstack1l1llll1l_opy_ (u"ࠤࠥગ")
  if not os.path.exists(bstack1ll1111ll_opy_):
    bstack1111ll1_opy_(
      bstack1111llll1_opy_.format(os.getcwd()))
  try:
    with open(bstack1ll1111ll_opy_, bstack1l1llll1l_opy_ (u"ࠪࡶࠬઘ")) as stream:
        yaml.add_implicit_resolver(bstack1l1llll1l_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧઙ"), bstack1111111_opy_)
        yaml.add_constructor(bstack1l1llll1l_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨચ"), bstack1l111l1l1_opy_)
        config = yaml.load(stream, yaml.FullLoader)
        return config
  except:
    with open(bstack1ll1111ll_opy_, bstack1l1llll1l_opy_ (u"࠭ࡲࠨછ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1111ll1_opy_(bstack1llll_opy_.format(str(exc)))
def bstack1l1l11l11_opy_(config):
  bstack11l1ll1l1_opy_ = bstack1l1lll1ll_opy_(config)
  for option in list(bstack11l1ll1l1_opy_):
    if option.lower() in bstack1llll111l_opy_ and option != bstack1llll111l_opy_[option.lower()]:
      bstack11l1ll1l1_opy_[bstack1llll111l_opy_[option.lower()]] = bstack11l1ll1l1_opy_[option]
      del bstack11l1ll1l1_opy_[option]
  return config
def bstack1111lll1l_opy_():
  global bstack111l11111_opy_
  for key, bstack11l1lll1_opy_ in bstack1l1111l1l_opy_.items():
    if isinstance(bstack11l1lll1_opy_, list):
      for var in bstack11l1lll1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack111l11111_opy_[key] = os.environ[var]
          break
    elif bstack11l1lll1_opy_ in os.environ and os.environ[bstack11l1lll1_opy_] and str(os.environ[bstack11l1lll1_opy_]).strip():
      bstack111l11111_opy_[key] = os.environ[bstack11l1lll1_opy_]
  if bstack1l1llll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩજ") in os.environ:
    bstack111l11111_opy_[bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઝ")] = {}
    bstack111l11111_opy_[bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઞ")][bstack1l1llll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬટ")] = os.environ[bstack1l1llll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ઠ")]
def bstack11l1l111l_opy_():
  global bstack1l11l11_opy_
  global bstack11l1l1lll_opy_
  for idx, val in enumerate(sys.argv):
    if idx<len(sys.argv) and bstack1l1llll1l_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨડ").lower() == val.lower():
      bstack1l11l11_opy_[bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઢ")] = {}
      bstack1l11l11_opy_[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫણ")][bstack1l1llll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત")] = sys.argv[idx+1]
      del sys.argv[idx:idx+2]
      break
  for key, bstack1l1l11l_opy_ in bstack111111l_opy_.items():
    if isinstance(bstack1l1l11l_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1l1l11l_opy_:
          if idx<len(sys.argv) and bstack1l1llll1l_opy_ (u"ࠩ࠰࠱ࠬથ") + var.lower() == val.lower() and not key in bstack1l11l11_opy_:
            bstack1l11l11_opy_[key] = sys.argv[idx+1]
            bstack11l1l1lll_opy_ += bstack1l1llll1l_opy_ (u"ࠪࠤ࠲࠳ࠧદ") + var + bstack1l1llll1l_opy_ (u"ࠫࠥ࠭ધ") + sys.argv[idx+1]
            del sys.argv[idx:idx+2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx<len(sys.argv) and bstack1l1llll1l_opy_ (u"ࠬ࠳࠭ࠨન") + bstack1l1l11l_opy_.lower() == val.lower() and not key in bstack1l11l11_opy_:
          bstack1l11l11_opy_[key] = sys.argv[idx+1]
          bstack11l1l1lll_opy_ += bstack1l1llll1l_opy_ (u"࠭ࠠ࠮࠯ࠪ઩") + bstack1l1l11l_opy_ + bstack1l1llll1l_opy_ (u"ࠧࠡࠩપ") + sys.argv[idx+1]
          del sys.argv[idx:idx+2]
def bstack1lllllll_opy_(config):
  bstack1l11l1l1l_opy_ = config.keys()
  for bstack1111ll11_opy_, bstack1ll1l1_opy_ in bstack1ll11llll_opy_.items():
    if bstack1ll1l1_opy_ in bstack1l11l1l1l_opy_:
      config[bstack1111ll11_opy_] = config[bstack1ll1l1_opy_]
      del config[bstack1ll1l1_opy_]
  for bstack1111ll11_opy_, bstack1ll1l1_opy_ in bstack1ll11ll_opy_.items():
    if isinstance(bstack1ll1l1_opy_, list):
      for bstack11llll11l_opy_ in bstack1ll1l1_opy_:
        if bstack11llll11l_opy_ in bstack1l11l1l1l_opy_:
          config[bstack1111ll11_opy_] = config[bstack11llll11l_opy_]
          del config[bstack11llll11l_opy_]
          break
    elif bstack1ll1l1_opy_ in bstack1l11l1l1l_opy_:
        config[bstack1111ll11_opy_] = config[bstack1ll1l1_opy_]
        del config[bstack1ll1l1_opy_]
  for bstack11llll11l_opy_ in list(config):
    for bstack1ll_opy_ in bstack1l11l11ll_opy_:
      if bstack11llll11l_opy_.lower() == bstack1ll_opy_.lower() and bstack11llll11l_opy_ != bstack1ll_opy_:
        config[bstack1ll_opy_] = config[bstack11llll11l_opy_]
        del config[bstack11llll11l_opy_]
  bstack111l111l_opy_ = []
  if bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫફ") in config:
    bstack111l111l_opy_ = config[bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬબ")]
  for platform in bstack111l111l_opy_:
    for bstack11llll11l_opy_ in list(platform):
      for bstack1ll_opy_ in bstack1l11l11ll_opy_:
        if bstack11llll11l_opy_.lower() == bstack1ll_opy_.lower() and bstack11llll11l_opy_ != bstack1ll_opy_:
          platform[bstack1ll_opy_] = platform[bstack11llll11l_opy_]
          del platform[bstack11llll11l_opy_]
  for bstack1111ll11_opy_, bstack1ll1l1_opy_ in bstack1ll11ll_opy_.items():
    for platform in bstack111l111l_opy_:
      if isinstance(bstack1ll1l1_opy_, list):
        for bstack11llll11l_opy_ in bstack1ll1l1_opy_:
          if bstack11llll11l_opy_ in platform:
            platform[bstack1111ll11_opy_] = platform[bstack11llll11l_opy_]
            del platform[bstack11llll11l_opy_]
            break
      elif bstack1ll1l1_opy_ in platform:
        platform[bstack1111ll11_opy_] = platform[bstack1ll1l1_opy_]
        del platform[bstack1ll1l1_opy_]
  for bstack11l111l11_opy_ in bstack111ll1_opy_:
    if bstack11l111l11_opy_ in config:
      if not bstack111ll1_opy_[bstack11l111l11_opy_] in config:
        config[bstack111ll1_opy_[bstack11l111l11_opy_]] = {}
      config[bstack111ll1_opy_[bstack11l111l11_opy_]].update(config[bstack11l111l11_opy_])
      del config[bstack11l111l11_opy_]
  for platform in bstack111l111l_opy_:
    for bstack11l111l11_opy_ in bstack111ll1_opy_:
      if bstack11l111l11_opy_ in list(platform):
        if not bstack111ll1_opy_[bstack11l111l11_opy_] in platform:
          platform[bstack111ll1_opy_[bstack11l111l11_opy_]] = {}
        platform[bstack111ll1_opy_[bstack11l111l11_opy_]].update(platform[bstack11l111l11_opy_])
        del platform[bstack11l111l11_opy_]
  config = bstack1l1l11l11_opy_(config)
  return config
def bstack111l1ll11_opy_(config):
  global bstack11l1l111_opy_
  if bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧભ") in config and str(config[bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨમ")]).lower() != bstack1l1llll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫય"):
    if not bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪર") in config:
      config[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઱")] = {}
    if not bstack1l1llll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ") in config[bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ળ")]:
      bstack1l11ll1l1_opy_ = datetime.datetime.now()
      bstack1ll1l111l_opy_ = bstack1l11ll1l1_opy_.strftime(bstack1l1llll1l_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧ઴"))
      hostname = socket.gethostname()
      bstack1l11l11l_opy_ = bstack1l1llll1l_opy_ (u"ࠫࠬવ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l1llll1l_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧશ").format(bstack1ll1l111l_opy_, hostname, bstack1l11l11l_opy_)
      config[bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪષ")][bstack1l1llll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩસ")] = identifier
    bstack11l1l111_opy_ = config[bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬહ")][bstack1l1llll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ઺")]
  return config
def bstack1l1l1l1l_opy_():
  if (
    isinstance(os.getenv(bstack1l1llll1l_opy_ (u"ࠪࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠨ઻")), str) and len(os.getenv(bstack1l1llll1l_opy_ (u"ࠫࡏࡋࡎࡌࡋࡑࡗࡤ࡛ࡒࡍ઼ࠩ"))) > 0
  ) or (
    isinstance(os.getenv(bstack1l1llll1l_opy_ (u"ࠬࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠫઽ")), str) and len(os.getenv(bstack1l1llll1l_opy_ (u"࠭ࡊࡆࡐࡎࡍࡓ࡙࡟ࡉࡑࡐࡉࠬા"))) > 0
  ):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠧࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗ࠭િ"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠨࡅࡌࠫી"))).lower() == bstack1l1llll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧુ") and str(os.getenv(bstack1l1llll1l_opy_ (u"ࠪࡇࡎࡘࡃࡍࡇࡆࡍࠬૂ"))).lower() == bstack1l1llll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩૃ"):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠬࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࠨૄ"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"࠭ࡃࡊࠩૅ"))).lower() == bstack1l1llll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ૆") and str(os.getenv(bstack1l1llll1l_opy_ (u"ࠨࡖࡕࡅ࡛ࡏࡓࠨે"))).lower() == bstack1l1llll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧૈ"):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠪࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠩૉ"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠫࡈࡏࠧ૊"))).lower() == bstack1l1llll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪો") and str(os.getenv(bstack1l1llll1l_opy_ (u"࠭ࡃࡊࡡࡑࡅࡒࡋࠧૌ"))).lower() == bstack1l1llll1l_opy_ (u"ࠧࡤࡱࡧࡩࡸ࡮ࡩࡱ્ࠩ"):
    return 0 # bstack1lll1l1l1_opy_ bstack111l11ll1_opy_ not set build number env
  if os.getenv(bstack1l1llll1l_opy_ (u"ࠨࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡇࡘࡁࡏࡅࡋࠫ૎")) and os.getenv(bstack1l1llll1l_opy_ (u"ࠩࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡉࡏࡎࡏࡌࡘࠬ૏")):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠪࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠬૐ"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠫࡈࡏࠧ૑"))).lower() == bstack1l1llll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪ૒") and str(os.getenv(bstack1l1llll1l_opy_ (u"࠭ࡄࡓࡑࡑࡉࠬ૓"))).lower() == bstack1l1llll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬ૔"):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠨࡆࡕࡓࡓࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗ࠭૕"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠩࡆࡍࠬ૖"))).lower() == bstack1l1llll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨ૗") and str(os.getenv(bstack1l1llll1l_opy_ (u"ࠫࡘࡋࡍࡂࡒࡋࡓࡗࡋࠧ૘"))).lower() == bstack1l1llll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪ૙"):
    return os.getenv(bstack1l1llll1l_opy_ (u"࠭ࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡍࡓࡇࡥࡉࡅࠩ૚"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠧࡄࡋࠪ૛"))).lower() == bstack1l1llll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭૜") and str(os.getenv(bstack1l1llll1l_opy_ (u"ࠩࡊࡍ࡙ࡒࡁࡃࡡࡆࡍࠬ૝"))).lower() == bstack1l1llll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨ૞"):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠫࡈࡏ࡟ࡋࡑࡅࡣࡎࡊࠧ૟"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠬࡉࡉࠨૠ"))).lower() == bstack1l1llll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫૡ") and str(os.getenv(bstack1l1llll1l_opy_ (u"ࠧࡃࡗࡌࡐࡉࡑࡉࡕࡇࠪૢ"))).lower() == bstack1l1llll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ૣ"):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠩࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠫ૤"), 0)
  if str(os.getenv(bstack1l1llll1l_opy_ (u"ࠪࡘࡋࡥࡂࡖࡋࡏࡈࠬ૥"))).lower() == bstack1l1llll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ૦"):
    return os.getenv(bstack1l1llll1l_opy_ (u"ࠬࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠬ૧"), 0)
  return -1
def bstack11lll11ll_opy_(bstack1l1ll1_opy_):
  global CONFIG
  if not bstack1l1llll1l_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨ૨") in CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૩")]:
    return
  CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૪")] = CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૫")].replace(
    bstack1l1llll1l_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ૬"),
    str(bstack1l1ll1_opy_)
  )
def bstack1l1l1l1l1_opy_():
  global CONFIG
  if not bstack1l1llll1l_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪ૭") in CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૮")]:
    return
  bstack1l11ll1l1_opy_ = datetime.datetime.now()
  bstack1ll1l111l_opy_ = bstack1l11ll1l1_opy_.strftime(bstack1l1llll1l_opy_ (u"࠭ࠥࡥ࠯ࠨࡦ࠲ࠫࡈ࠻ࠧࡐࠫ૯"))
  CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૰")] = CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૱")].replace(
    bstack1l1llll1l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨ૲"),
    bstack1ll1l111l_opy_
  )
def bstack11lllllll_opy_():
  global CONFIG
  if bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૳") in CONFIG and not bool(CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૴")]):
    del CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૵")]
    return
  if not bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૶") in CONFIG:
    CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૷")] = bstack1l1llll1l_opy_ (u"ࠨࠥࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫ૸")
  if bstack1l1llll1l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨૹ") in CONFIG[bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૺ")]:
    bstack1l1l1l1l1_opy_()
    os.environ[bstack1l1llll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨૻ")] = CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૼ")]
  if not bstack1l1llll1l_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨ૽") in CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૾")]:
    return
  bstack1l1ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࠩ૿")
  bstack11ll11ll1_opy_ = bstack1l1l1l1l_opy_()
  if bstack11ll11ll1_opy_ != -1:
    bstack1l1ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡆࡍࠥ࠭଀") + str(bstack11ll11ll1_opy_)
  if bstack1l1ll1_opy_ == bstack1l1llll1l_opy_ (u"ࠪࠫଁ"):
    bstack1lllll11l_opy_ = bstack111l1llll_opy_(CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧଂ")])
    if bstack1lllll11l_opy_ != -1:
      bstack1l1ll1_opy_ = str(bstack1lllll11l_opy_)
  if bstack1l1ll1_opy_:
    bstack11lll11ll_opy_(bstack1l1ll1_opy_)
    os.environ[bstack1l1llll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩଃ")] = CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ଄")]
def bstack1llllll11_opy_(bstack11llllll1_opy_, bstack111ll1ll_opy_, path):
  bstack1l1ll11_opy_ = {
    bstack1l1llll1l_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫଅ"): bstack111ll1ll_opy_
  }
  if os.path.exists(path):
    bstack1l11l1l1_opy_ = json.load(open(path, bstack1l1llll1l_opy_ (u"ࠨࡴࡥࠫଆ")))
  else:
    bstack1l11l1l1_opy_ = {}
  bstack1l11l1l1_opy_[bstack11llllll1_opy_] = bstack1l1ll11_opy_
  with open(path, bstack1l1llll1l_opy_ (u"ࠤࡺ࠯ࠧଇ")) as outfile:
    json.dump(bstack1l11l1l1_opy_, outfile)
def bstack111l1llll_opy_(bstack11llllll1_opy_):
  bstack11llllll1_opy_ = str(bstack11llllll1_opy_)
  bstack1ll11l1_opy_ = os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠪࢂࠬଈ")), bstack1l1llll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫଉ"))
  try:
    if not os.path.exists(bstack1ll11l1_opy_):
      os.makedirs(bstack1ll11l1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠬࢄࠧଊ")), bstack1l1llll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ଋ"), bstack1l1llll1l_opy_ (u"ࠧ࠯ࡤࡸ࡭ࡱࡪ࠭࡯ࡣࡰࡩ࠲ࡩࡡࡤࡪࡨ࠲࡯ࡹ࡯࡯ࠩଌ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l1llll1l_opy_ (u"ࠨࡹࠪ଍")):
        pass
      with open(file_path, bstack1l1llll1l_opy_ (u"ࠤࡺ࠯ࠧ଎")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l1llll1l_opy_ (u"ࠪࡶࠬଏ")) as bstack111llllll_opy_:
      bstack111ll1l11_opy_ = json.load(bstack111llllll_opy_)
    if bstack11llllll1_opy_ in bstack111ll1l11_opy_:
      bstack11l1_opy_ = bstack111ll1l11_opy_[bstack11llllll1_opy_][bstack1l1llll1l_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨଐ")]
      bstack1ll11l111_opy_ = int(bstack11l1_opy_) + 1
      bstack1llllll11_opy_(bstack11llllll1_opy_, bstack1ll11l111_opy_, file_path)
      return bstack1ll11l111_opy_
    else:
      bstack1llllll11_opy_(bstack11llllll1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1ll1lll_opy_.format(str(e)))
    return -1
def bstack11lll11_opy_(config):
  if not config[bstack1l1llll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ଑")] or not config[bstack1l1llll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ଒")]:
    return True
  else:
    return False
def bstack111l1l_opy_(config):
  if bstack1l1llll1l_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ଓ") in config:
    del(config[bstack1l1llll1l_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧଔ")])
    return False
  if bstack11lll1111_opy_() < version.parse(bstack1l1llll1l_opy_ (u"ࠩ࠶࠲࠹࠴࠰ࠨକ")):
    return False
  if bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠪ࠸࠳࠷࠮࠶ࠩଖ")):
    return True
  if bstack1l1llll1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫଗ") in config and config[bstack1l1llll1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଘ")] == False:
    return False
  else:
    return True
def bstack11ll1111l_opy_(config, index = 0):
  global bstack111l1l111_opy_
  bstack11ll1111_opy_ = {}
  caps = bstack11ll1ll1l_opy_ + bstack11l11l1_opy_
  if bstack111l1l111_opy_:
    caps += bstack111l1_opy_
  for key in config:
    if key in caps + [bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଙ")]:
      continue
    bstack11ll1111_opy_[key] = config[key]
  if bstack1l1llll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଚ") in config:
    for bstack11l1ll11l_opy_ in config[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଛ")][index]:
      if bstack11l1ll11l_opy_ in caps + [bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଜ"), bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫଝ")]:
        continue
      bstack11ll1111_opy_[bstack11l1ll11l_opy_] = config[bstack1l1llll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଞ")][index][bstack11l1ll11l_opy_]
  bstack11ll1111_opy_[bstack1l1llll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧଟ")] = socket.gethostname()
  if bstack1l1llll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧଠ") in bstack11ll1111_opy_:
    del(bstack11ll1111_opy_[bstack1l1llll1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨଡ")])
  return bstack11ll1111_opy_
def bstack1lll1_opy_(config):
  global bstack111l1l111_opy_
  bstack111l11ll_opy_ = {}
  caps = bstack11l11l1_opy_
  if bstack111l1l111_opy_:
    caps+= bstack111l1_opy_
  for key in caps:
    if key in config:
      bstack111l11ll_opy_[key] = config[key]
  return bstack111l11ll_opy_
def bstack11lll1_opy_(bstack11ll1111_opy_, bstack111l11ll_opy_):
  bstack1l1ll111_opy_ = {}
  for key in bstack11ll1111_opy_.keys():
    if key in bstack1ll11llll_opy_:
      bstack1l1ll111_opy_[bstack1ll11llll_opy_[key]] = bstack11ll1111_opy_[key]
    else:
      bstack1l1ll111_opy_[key] = bstack11ll1111_opy_[key]
  for key in bstack111l11ll_opy_:
    if key in bstack1ll11llll_opy_:
      bstack1l1ll111_opy_[bstack1ll11llll_opy_[key]] = bstack111l11ll_opy_[key]
    else:
      bstack1l1ll111_opy_[key] = bstack111l11ll_opy_[key]
  return bstack1l1ll111_opy_
def bstack11ll11111_opy_(config, index = 0):
  global bstack111l1l111_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack111l11ll_opy_ = bstack1lll1_opy_(config)
  bstack1111l1l_opy_ = bstack11l11l1_opy_
  bstack1111l1l_opy_ += bstack11l11111l_opy_
  if bstack111l1l111_opy_:
    bstack1111l1l_opy_ += bstack111l1_opy_
  if bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଢ") in config:
    if bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଣ") in config[bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ତ")][index]:
      caps[bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଥ")] = config[bstack1l1llll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଦ")][index][bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଧ")]
    if bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨନ") in config[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଩")][index]:
      caps[bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪପ")] = str(config[bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଫ")][index][bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬବ")])
    bstack1l1llllll_opy_ = {}
    for bstack1l11lll1_opy_ in bstack1111l1l_opy_:
      if bstack1l11lll1_opy_ in config[bstack1l1llll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଭ")][index]:
        if bstack1l11lll1_opy_ == bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨମ"):
          try:
            bstack1l1llllll_opy_[bstack1l11lll1_opy_] = str(config[bstack1l1llll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଯ")][index][bstack1l11lll1_opy_] * 1.0)
          except:
            bstack1l1llllll_opy_[bstack1l11lll1_opy_] = str(config[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫର")][index][bstack1l11lll1_opy_])
        else:
          bstack1l1llllll_opy_[bstack1l11lll1_opy_] = config[bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଱")][index][bstack1l11lll1_opy_]
        del(config[bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଲ")][index][bstack1l11lll1_opy_])
    bstack111l11ll_opy_ = update(bstack111l11ll_opy_, bstack1l1llllll_opy_)
  bstack11ll1111_opy_ = bstack11ll1111l_opy_(config, index)
  for bstack11llll11l_opy_ in bstack11l11l1_opy_ + [bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଳ"), bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭଴")]:
    if bstack11llll11l_opy_ in bstack11ll1111_opy_:
      bstack111l11ll_opy_[bstack11llll11l_opy_] = bstack11ll1111_opy_[bstack11llll11l_opy_]
      del(bstack11ll1111_opy_[bstack11llll11l_opy_])
  if bstack111l1l_opy_(config):
    bstack11ll1111_opy_[bstack1l1llll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ଵ")] = True
    caps.update(bstack111l11ll_opy_)
    caps[bstack1l1llll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଶ")] = bstack11ll1111_opy_
  else:
    bstack11ll1111_opy_[bstack1l1llll1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨଷ")] = False
    caps.update(bstack11lll1_opy_(bstack11ll1111_opy_, bstack111l11ll_opy_))
    if bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧସ") in caps:
      caps[bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫହ")] = caps[bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ଺")]
      del(caps[bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଻")])
    if bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴ଼ࠧ") in caps:
      caps[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩଽ")] = caps[bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩା")]
      del(caps[bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪି")])
  return caps
def bstack111ll_opy_():
  global bstack1ll1lll_opy_
  if bstack11lll1111_opy_() <= version.parse(bstack1l1llll1l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪୀ")):
    if bstack1ll1lll_opy_ != bstack1l1llll1l_opy_ (u"ࠫࠬୁ"):
      return bstack1l1llll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨୂ") + bstack1ll1lll_opy_ + bstack1l1llll1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥୃ")
    return bstack11ll11lll_opy_
  if  bstack1ll1lll_opy_ != bstack1l1llll1l_opy_ (u"ࠧࠨୄ"):
    return bstack1l1llll1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ୅") + bstack1ll1lll_opy_ + bstack1l1llll1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ୆")
  return bstack1llllll1_opy_
def bstack1lll11111_opy_(options):
  return hasattr(options, bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫେ"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1lll11l_opy_(options, bstack111lll1ll_opy_):
  for bstack1l111ll11_opy_ in bstack111lll1ll_opy_:
    if bstack1l111ll11_opy_ in [bstack1l1llll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩୈ"), bstack1l1llll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ୉")]:
      next
    if bstack1l111ll11_opy_ in options._experimental_options:
      options._experimental_options[bstack1l111ll11_opy_]= update(options._experimental_options[bstack1l111ll11_opy_], bstack111lll1ll_opy_[bstack1l111ll11_opy_])
    else:
      options.add_experimental_option(bstack1l111ll11_opy_, bstack111lll1ll_opy_[bstack1l111ll11_opy_])
  if bstack1l1llll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ୊") in bstack111lll1ll_opy_:
    for arg in bstack111lll1ll_opy_[bstack1l1llll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬୋ")]:
      options.add_argument(arg)
    del(bstack111lll1ll_opy_[bstack1l1llll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ୌ")])
  if bstack1l1llll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ୍࠭") in bstack111lll1ll_opy_:
    for ext in bstack111lll1ll_opy_[bstack1l1llll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ୎")]:
      options.add_extension(ext)
    del(bstack111lll1ll_opy_[bstack1l1llll1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ୏")])
def bstack1ll111l1_opy_(options, bstack1111lll_opy_):
  if bstack1l1llll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ୐") in bstack1111lll_opy_:
    for bstack1l1ll_opy_ in bstack1111lll_opy_[bstack1l1llll1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ୑")]:
      if bstack1l1ll_opy_ in options._preferences:
        options._preferences[bstack1l1ll_opy_] = update(options._preferences[bstack1l1ll_opy_], bstack1111lll_opy_[bstack1l1llll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭୒")][bstack1l1ll_opy_])
      else:
        options.set_preference(bstack1l1ll_opy_, bstack1111lll_opy_[bstack1l1llll1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ୓")][bstack1l1ll_opy_])
  if bstack1l1llll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ୔") in bstack1111lll_opy_:
    for arg in bstack1111lll_opy_[bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ୕")]:
      options.add_argument(arg)
def bstack111ll11l_opy_(options, bstack1111lll11_opy_):
  if bstack1l1llll1l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬୖ") in bstack1111lll11_opy_:
    options.use_webview(bool(bstack1111lll11_opy_[bstack1l1llll1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭ୗ")]))
  bstack1lll11l_opy_(options, bstack1111lll11_opy_)
def bstack11ll1llll_opy_(options, bstack11llll1l_opy_):
  for bstack1l1l11lll_opy_ in bstack11llll1l_opy_:
    if bstack1l1l11lll_opy_ in [bstack1l1llll1l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪ୘"), bstack1l1llll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ୙")]:
      next
    options.set_capability(bstack1l1l11lll_opy_, bstack11llll1l_opy_[bstack1l1l11lll_opy_])
  if bstack1l1llll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭୚") in bstack11llll1l_opy_:
    for arg in bstack11llll1l_opy_[bstack1l1llll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ୛")]:
      options.add_argument(arg)
  if bstack1l1llll1l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଡ଼") in bstack11llll1l_opy_:
    options.bstack1l1l1llll_opy_(bool(bstack11llll1l_opy_[bstack1l1llll1l_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଢ଼")]))
def bstack1l1l1l11_opy_(options, bstack1l1ll11l_opy_):
  for bstack1lll11_opy_ in bstack1l1ll11l_opy_:
    if bstack1lll11_opy_ in [bstack1l1llll1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୞"), bstack1l1llll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫୟ")]:
      next
    options._options[bstack1lll11_opy_] = bstack1l1ll11l_opy_[bstack1lll11_opy_]
  if bstack1l1llll1l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫୠ") in bstack1l1ll11l_opy_:
    for bstack1ll1_opy_ in bstack1l1ll11l_opy_[bstack1l1llll1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬୡ")]:
      options.bstack1ll1111l1_opy_(
          bstack1ll1_opy_, bstack1l1ll11l_opy_[bstack1l1llll1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ୢ")][bstack1ll1_opy_])
  if bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨୣ") in bstack1l1ll11l_opy_:
    for arg in bstack1l1ll11l_opy_[bstack1l1llll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ୤")]:
      options.add_argument(arg)
def bstack1lll1l11l_opy_(options, caps):
  if not hasattr(options, bstack1l1llll1l_opy_ (u"ࠬࡑࡅ࡚ࠩ୥")):
    return
  if options.KEY == bstack1l1llll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ୦") and options.KEY in caps:
    bstack1lll11l_opy_(options, caps[bstack1l1llll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ୧")])
  elif options.KEY == bstack1l1llll1l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭୨") and options.KEY in caps:
    bstack1ll111l1_opy_(options, caps[bstack1l1llll1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ୩")])
  elif options.KEY == bstack1l1llll1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫ୪") and options.KEY in caps:
    bstack11ll1llll_opy_(options, caps[bstack1l1llll1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ୫")])
  elif options.KEY == bstack1l1llll1l_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୬") and options.KEY in caps:
    bstack111ll11l_opy_(options, caps[bstack1l1llll1l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୭")])
  elif options.KEY == bstack1l1llll1l_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୮") and options.KEY in caps:
    bstack1l1l1l11_opy_(options, caps[bstack1l1llll1l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୯")])
def bstack11ll11ll_opy_(caps):
  global bstack111l1l111_opy_
  if bstack111l1l111_opy_:
    if bstack11l111111_opy_() < version.parse(bstack1l1llll1l_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨ୰")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l1llll1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪୱ")
    if bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ୲") in caps:
      browser = caps[bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୳")]
    elif bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ୴") in caps:
      browser = caps[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ୵")]
    browser = str(browser).lower()
    if browser == bstack1l1llll1l_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨ୶") or browser == bstack1l1llll1l_opy_ (u"ࠩ࡬ࡴࡦࡪࠧ୷"):
      browser = bstack1l1llll1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪ୸")
    if browser == bstack1l1llll1l_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬ୹"):
      browser = bstack1l1llll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୺")
    if browser not in [bstack1l1llll1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୻"), bstack1l1llll1l_opy_ (u"ࠧࡦࡦࡪࡩࠬ୼"), bstack1l1llll1l_opy_ (u"ࠨ࡫ࡨࠫ୽"), bstack1l1llll1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ୾"), bstack1l1llll1l_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫ୿")]:
      return None
    try:
      package = bstack1l1llll1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭஀").format(browser)
      name = bstack1l1llll1l_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭஁")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1lll11111_opy_(options):
        return None
      for bstack11llll11l_opy_ in caps.keys():
        options.set_capability(bstack11llll11l_opy_, caps[bstack11llll11l_opy_])
      bstack1lll1l11l_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l1ll11ll_opy_(options, bstack1llll11ll_opy_):
  if not bstack1lll11111_opy_(options):
    return
  for bstack11llll11l_opy_ in bstack1llll11ll_opy_.keys():
    if bstack11llll11l_opy_ in bstack11l11111l_opy_:
      next
    if bstack11llll11l_opy_ in options._caps and type(options._caps[bstack11llll11l_opy_]) in [dict, list]:
      options._caps[bstack11llll11l_opy_] = update(options._caps[bstack11llll11l_opy_], bstack1llll11ll_opy_[bstack11llll11l_opy_])
    else:
      options.set_capability(bstack11llll11l_opy_, bstack1llll11ll_opy_[bstack11llll11l_opy_])
  bstack1lll1l11l_opy_(options, bstack1llll11ll_opy_)
  if bstack1l1llll1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬஂ") in options._caps:
    if options._caps[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬஃ")] and options._caps[bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭஄")].lower() != bstack1l1llll1l_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪஅ"):
      del options._caps[bstack1l1llll1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩஆ")]
def bstack1l111l11l_opy_(proxy_config):
  if bstack1l1llll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨஇ") in proxy_config:
    proxy_config[bstack1l1llll1l_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧஈ")] = proxy_config[bstack1l1llll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪஉ")]
    del(proxy_config[bstack1l1llll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫஊ")])
  if bstack1l1llll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ஋") in proxy_config and proxy_config[bstack1l1llll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ஌")].lower() != bstack1l1llll1l_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪ஍"):
    proxy_config[bstack1l1llll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧஎ")] = bstack1l1llll1l_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬஏ")
  if bstack1l1llll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫஐ") in proxy_config:
    proxy_config[bstack1l1llll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ஑")] = bstack1l1llll1l_opy_ (u"ࠨࡲࡤࡧࠬஒ")
  return proxy_config
def bstack11llll11_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l1llll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨஓ") in config:
    return proxy
  config[bstack1l1llll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩஔ")] = bstack1l111l11l_opy_(config[bstack1l1llll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪக")])
  if proxy == None:
    proxy = Proxy(config[bstack1l1llll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ஖")])
  return proxy
def bstack11l1l1_opy_(self):
  global CONFIG
  global bstack1lllll111_opy_
  try:
    proxy = bstack1ll1ll11_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l1llll1l_opy_ (u"࠭࠮ࡱࡣࡦࠫ஗")):
        proxies = bstack1l1l1111l_opy_(proxy, bstack111ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1llll111_opy_ = proxies.popitem()
          if bstack1l1llll1l_opy_ (u"ࠢ࠻࠱࠲ࠦ஘") in bstack1llll111_opy_:
            return bstack1llll111_opy_
          else:
            return bstack1l1llll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤங") + bstack1llll111_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l1llll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨச").format(str(e)))
  return bstack1lllll111_opy_(self)
def bstack111l1lll_opy_():
  global CONFIG
  return bstack1l1llll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭஛") in CONFIG or bstack1l1llll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨஜ") in CONFIG
def bstack1ll1ll11_opy_(config):
  if not bstack111l1lll_opy_():
    return
  if config.get(bstack1l1llll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ஝")):
    return config.get(bstack1l1llll1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩஞ"))
  if config.get(bstack1l1llll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫட")):
    return config.get(bstack1l1llll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ஠"))
def bstack11ll11_opy_(url):
  try:
      result = urlparse(url)
      return all([result.scheme, result.netloc])
  except:
      return False
def bstack111l11_opy_(bstack1l1l11111_opy_, bstack11l111ll_opy_):
  from pypac import get_pac
  from pypac import PACSession
  from pypac.parser import PACFile
  import socket
  if os.path.isfile(bstack1l1l11111_opy_):
    with open(bstack1l1l11111_opy_) as f:
      pac = PACFile(f.read())
  elif bstack11ll11_opy_(bstack1l1l11111_opy_):
    pac = get_pac(url=bstack1l1l11111_opy_)
  else:
    raise Exception(bstack1l1llll1l_opy_ (u"ࠩࡓࡥࡨࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠩ஡").format(bstack1l1l11111_opy_))
  session = PACSession(pac)
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((bstack1l1llll1l_opy_ (u"ࠥ࠼࠳࠾࠮࠹࠰࠻ࠦ஢"), 80))
    bstack1ll1ll1l1_opy_ = s.getsockname()[0]
    s.close()
  except:
    bstack1ll1ll1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠫ࠵࠴࠰࠯࠲࠱࠴ࠬண")
  proxy_url = session.get_pac().find_proxy_for_url(bstack11l111ll_opy_, bstack1ll1ll1l1_opy_)
  return proxy_url
def bstack1l1l1111l_opy_(bstack1l1l11111_opy_, bstack11l111ll_opy_):
  proxies = {}
  global bstack1llll1l1l_opy_
  if bstack1l1llll1l_opy_ (u"ࠬࡖࡁࡄࡡࡓࡖࡔ࡞࡙ࠨத") in globals():
    return bstack1llll1l1l_opy_
  try:
    proxy = bstack111l11_opy_(bstack1l1l11111_opy_,bstack11l111ll_opy_)
    if bstack1l1llll1l_opy_ (u"ࠨࡄࡊࡔࡈࡇ࡙ࠨ஥") in proxy:
      proxies = {}
    elif bstack1l1llll1l_opy_ (u"ࠢࡉࡖࡗࡔࠧ஦") in proxy or bstack1l1llll1l_opy_ (u"ࠣࡊࡗࡘࡕ࡙ࠢ஧") in proxy or bstack1l1llll1l_opy_ (u"ࠤࡖࡓࡈࡑࡓࠣந") in proxy:
      bstack1l11l1_opy_ = proxy.split(bstack1l1llll1l_opy_ (u"ࠥࠤࠧன"))
      if bstack1l1llll1l_opy_ (u"ࠦ࠿࠵࠯ࠣப") in bstack1l1llll1l_opy_ (u"ࠧࠨ஫").join(bstack1l11l1_opy_[1:]):
        proxies = {
          bstack1l1llll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ஬"): bstack1l1llll1l_opy_ (u"ࠢࠣ஭").join(bstack1l11l1_opy_[1:])
        }
      else:
        proxies = {
          bstack1l1llll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧம") : str(bstack1l11l1_opy_[0]).lower()+ bstack1l1llll1l_opy_ (u"ࠤ࠽࠳࠴ࠨய") + bstack1l1llll1l_opy_ (u"ࠥࠦர").join(bstack1l11l1_opy_[1:])
        }
    elif bstack1l1llll1l_opy_ (u"ࠦࡕࡘࡏ࡙࡛ࠥற") in proxy:
      bstack1l11l1_opy_ = proxy.split(bstack1l1llll1l_opy_ (u"ࠧࠦࠢல"))
      if bstack1l1llll1l_opy_ (u"ࠨ࠺࠰࠱ࠥள") in bstack1l1llll1l_opy_ (u"ࠢࠣழ").join(bstack1l11l1_opy_[1:]):
        proxies = {
          bstack1l1llll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧவ"): bstack1l1llll1l_opy_ (u"ࠤࠥஶ").join(bstack1l11l1_opy_[1:])
        }
      else:
        proxies = {
          bstack1l1llll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩஷ"): bstack1l1llll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧஸ") + bstack1l1llll1l_opy_ (u"ࠧࠨஹ").join(bstack1l11l1_opy_[1:])
        }
    else:
      proxies = {
        bstack1l1llll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ஺"): proxy
      }
  except Exception as e:
    logger.error(bstack11l11lll_opy_.format(bstack1l1l11111_opy_, str(e)))
  bstack1llll1l1l_opy_ = proxies
  return proxies
def bstack1_opy_(config, bstack11l111ll_opy_):
  proxy = bstack1ll1ll11_opy_(config)
  proxies = {}
  if config.get(bstack1l1llll1l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ஻")) or config.get(bstack1l1llll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ஼")):
    if proxy.endswith(bstack1l1llll1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ஽")):
      proxies = bstack1l1l1111l_opy_(proxy,bstack11l111ll_opy_)
    else:
      proxies = {
        bstack1l1llll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩா"): proxy
      }
  return proxies
def bstack11llll1l1_opy_():
  return bstack111l1lll_opy_() and bstack11lll1111_opy_() >= version.parse(bstack11l_opy_)
def bstack1l1lll1ll_opy_(config):
  bstack11l1ll1l1_opy_ = {}
  if bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨி") in config:
    bstack11l1ll1l1_opy_ =  config[bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩீ")]
  if bstack1l1llll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬு") in config:
    bstack11l1ll1l1_opy_ = config[bstack1l1llll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ூ")]
  proxy = bstack1ll1ll11_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l1llll1l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭௃")) and os.path.isfile(proxy):
      bstack11l1ll1l1_opy_[bstack1l1llll1l_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬ௄")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l1llll1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ௅")):
        proxies = bstack1_opy_(config, bstack111ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1llll111_opy_ = proxies.popitem()
          if bstack1l1llll1l_opy_ (u"ࠦ࠿࠵࠯ࠣெ") in bstack1llll111_opy_:
            parsed_url = urlparse(bstack1llll111_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l1llll1l_opy_ (u"ࠧࡀ࠯࠰ࠤே") + bstack1llll111_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l1ll1l1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩை")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l1ll1l1_opy_[bstack1l1llll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪ௉")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l1ll1l1_opy_[bstack1l1llll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫொ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l1ll1l1_opy_[bstack1l1llll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬோ")] = str(parsed_url.password)
  return bstack11l1ll1l1_opy_
def bstack1lll111l1_opy_(config):
  if bstack1l1llll1l_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨௌ") in config:
    return config[bstack1l1llll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴ்ࠩ")]
  return {}
def bstack111llll1l_opy_(caps):
  global bstack11l1l111_opy_
  if bstack1l1llll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭௎") in caps:
    caps[bstack1l1llll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ௏")][bstack1l1llll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ௐ")] = True
    if bstack11l1l111_opy_:
      caps[bstack1l1llll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ௑")][bstack1l1llll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௒")] = bstack11l1l111_opy_
  else:
    caps[bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨ௓")] = True
    if bstack11l1l111_opy_:
      caps[bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௔")] = bstack11l1l111_opy_
def bstack11ll11l1l_opy_():
  global CONFIG
  if bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ௕") in CONFIG and CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ௖")]:
    bstack11l1ll1l1_opy_ = bstack1l1lll1ll_opy_(CONFIG)
    bstack1lll1l_opy_(CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪௗ")], bstack11l1ll1l1_opy_)
def bstack1lll1l_opy_(key, bstack11l1ll1l1_opy_):
  global bstack11ll1l1l1_opy_
  logger.info(bstack1ll11111_opy_)
  try:
    bstack11ll1l1l1_opy_ = Local()
    bstack1lll1lll1_opy_ = {bstack1l1llll1l_opy_ (u"ࠨ࡭ࡨࡽࠬ௘"): key}
    bstack1lll1lll1_opy_.update(bstack11l1ll1l1_opy_)
    logger.debug(bstack1l1ll1l1l_opy_.format(str(bstack1lll1lll1_opy_)))
    bstack11ll1l1l1_opy_.start(**bstack1lll1lll1_opy_)
    if bstack11ll1l1l1_opy_.isRunning():
      logger.info(bstack1lll1l11_opy_)
  except Exception as e:
    bstack1111ll1_opy_(bstack111111ll_opy_.format(str(e)))
def bstackl_opy_():
  global bstack11ll1l1l1_opy_
  if bstack11ll1l1l1_opy_.isRunning():
    logger.info(bstack1ll11l_opy_)
    bstack11ll1l1l1_opy_.stop()
  bstack11ll1l1l1_opy_ = None
def bstack1l1l11_opy_(bstack111l111l1_opy_=[]):
  global CONFIG
  bstack1111llll_opy_ = []
  bstack1lll1l1l_opy_ = [bstack1l1llll1l_opy_ (u"ࠩࡲࡷࠬ௙"), bstack1l1llll1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭௚"), bstack1l1llll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ௛"), bstack1l1llll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ௜"), bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ௝"), bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ௞")]
  try:
    for err in bstack111l111l1_opy_:
      bstack1ll1l_opy_ = {}
      for k in bstack1lll1l1l_opy_:
        val = CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௟")][int(err[bstack1l1llll1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ௠")])].get(k)
        if val:
          bstack1ll1l_opy_[k] = val
      bstack1ll1l_opy_[bstack1l1llll1l_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩ௡")] = {
        err[bstack1l1llll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ௢")]: err[bstack1l1llll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ௣")]
      }
      bstack1111llll_opy_.append(bstack1ll1l_opy_)
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ௤") +str(e))
  finally:
    return bstack1111llll_opy_
def bstack1ll1l1ll1_opy_():
  global bstack11ll1l1ll_opy_
  global bstack1ll1l1ll_opy_
  global bstack11ll1l11_opy_
  if bstack11ll1l1ll_opy_:
    logger.warning(bstack1l1l111l_opy_.format(str(bstack11ll1l1ll_opy_)))
  logger.info(bstack1llll1_opy_)
  global bstack11ll1l1l1_opy_
  if bstack11ll1l1l1_opy_:
    bstackl_opy_()
  try:
    for driver in bstack1ll1l1ll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack111lll_opy_)
  bstack1llll11_opy_()
  if len(bstack11ll1l11_opy_) > 0:
    message = bstack1l1l11_opy_(bstack11ll1l11_opy_)
    bstack1llll11_opy_(message)
  else:
    bstack1llll11_opy_()
def bstack1lll1lll_opy_(self, *args):
  logger.error(bstack111l1l1l1_opy_)
  bstack1ll1l1ll1_opy_()
  sys.exit(1)
def bstack1111ll1_opy_(err):
  logger.critical(bstack111llll1_opy_.format(str(err)))
  bstack1llll11_opy_(bstack111llll1_opy_.format(str(err)))
  atexit.unregister(bstack1ll1l1ll1_opy_)
  sys.exit(1)
def bstack1ll1l1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1llll11_opy_(message)
  atexit.unregister(bstack1ll1l1ll1_opy_)
  sys.exit(1)
def bstack1lllll1_opy_():
  global CONFIG
  global bstack1l11l11_opy_
  global bstack111l11111_opy_
  global bstack11l11ll_opy_
  CONFIG = bstack11ll11l_opy_()
  bstack1111lll1l_opy_()
  bstack11l1l111l_opy_()
  CONFIG = bstack1lllllll_opy_(CONFIG)
  update(CONFIG, bstack111l11111_opy_)
  update(CONFIG, bstack1l11l11_opy_)
  CONFIG = bstack111l1ll11_opy_(CONFIG)
  if bstack1l1llll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ௥") in CONFIG and str(CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ௦")]).lower() == bstack1l1llll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ௧"):
    bstack11l11ll_opy_ = False
  if (bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௨") in CONFIG and bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௩") in bstack1l11l11_opy_) or (bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௪") in CONFIG and bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௫") not in bstack111l11111_opy_):
    if os.getenv(bstack1l1llll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௬")):
      CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௭")] = os.getenv(bstack1l1llll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭௮"))
    else:
      bstack11lllllll_opy_()
  elif (bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௯") not in CONFIG and bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௰") in CONFIG) or (bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௱") in bstack111l11111_opy_ and bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௲") not in bstack1l11l11_opy_):
    del(CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௳")])
  if bstack11lll11_opy_(CONFIG):
    bstack1111ll1_opy_(bstack111l11l1_opy_)
  bstack111ll1111_opy_()
  bstack1ll11111l_opy_()
  if bstack111l1l111_opy_:
    CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡣࡳࡴࠬ௴")] = bstack11l11l1ll_opy_(CONFIG)
    logger.info(bstack11ll111l1_opy_.format(CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵ࠭௵")]))
def bstack1ll11111l_opy_():
  global CONFIG
  global bstack111l1l111_opy_
  if bstack1l1llll1l_opy_ (u"ࠪࡥࡵࡶࠧ௶") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1l111l11_opy_)
    bstack111l1l111_opy_ = True
def bstack11l11l1ll_opy_(config):
  bstack11l1lll11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࠬ௷")
  app = config[bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡱࠩ௸")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11l11ll1_opy_:
      if os.path.exists(app):
        bstack11l1lll11_opy_ = bstack1l1l11l1_opy_(config, app)
      elif bstack11lll1l_opy_(app):
        bstack11l1lll11_opy_ = app
      else:
        bstack1111ll1_opy_(bstack1l1l11l1l_opy_.format(app))
    else:
      if bstack11lll1l_opy_(app):
        bstack11l1lll11_opy_ = app
      elif os.path.exists(app):
        bstack11l1lll11_opy_ = bstack1l1l11l1_opy_(app)
      else:
        bstack1111ll1_opy_(bstack11l1l11l1_opy_)
  else:
    if len(app) > 2:
      bstack1111ll1_opy_(bstack1llllllll_opy_)
    elif len(app) == 2:
      if bstack1l1llll1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௹") in app and bstack1l1llll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ௺") in app:
        if os.path.exists(app[bstack1l1llll1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭௻")]):
          bstack11l1lll11_opy_ = bstack1l1l11l1_opy_(config, app[bstack1l1llll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௼")], app[bstack1l1llll1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௽")])
        else:
          bstack1111ll1_opy_(bstack1l1l11l1l_opy_.format(app))
      else:
        bstack1111ll1_opy_(bstack1llllllll_opy_)
    else:
      for key in app:
        if key in bstack11lllll1l_opy_:
          if key == bstack1l1llll1l_opy_ (u"ࠫࡵࡧࡴࡩࠩ௾"):
            if os.path.exists(app[key]):
              bstack11l1lll11_opy_ = bstack1l1l11l1_opy_(config, app[key])
            else:
              bstack1111ll1_opy_(bstack1l1l11l1l_opy_.format(app))
          else:
            bstack11l1lll11_opy_ = app[key]
        else:
          bstack1111ll1_opy_(bstack1llllll_opy_)
  return bstack11l1lll11_opy_
def bstack11lll1l_opy_(bstack11l1lll11_opy_):
  import re
  bstack1llll1ll_opy_ = re.compile(bstack1l1llll1l_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௿"))
  bstack111111_opy_ = re.compile(bstack1l1llll1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥఀ"))
  if bstack1l1llll1l_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭ఁ") in bstack11l1lll11_opy_ or re.fullmatch(bstack1llll1ll_opy_, bstack11l1lll11_opy_) or re.fullmatch(bstack111111_opy_, bstack11l1lll11_opy_):
    return True
  else:
    return False
def bstack1l1l11l1_opy_(config, path, bstack11l1l1l11_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l1llll1l_opy_ (u"ࠨࡴࡥࠫం")).read()).hexdigest()
  bstack1l1l1lll_opy_ = bstack111l1l11l_opy_(md5_hash)
  bstack11l1lll11_opy_ = None
  if bstack1l1l1lll_opy_:
    logger.info(bstack1l11l1ll1_opy_.format(bstack1l1l1lll_opy_, md5_hash))
    return bstack1l1l1lll_opy_
  bstack1ll11lll1_opy_ = MultipartEncoder(
    fields={
        bstack1l1llll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧః"): (os.path.basename(path), open(os.path.abspath(path), bstack1l1llll1l_opy_ (u"ࠪࡶࡧ࠭ఄ")), bstack1l1llll1l_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨఅ")),
        bstack1l1llll1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨఆ"): bstack11l1l1l11_opy_
    }
  )
  response = requests.post(bstack1ll1l11l1_opy_, data=bstack1ll11lll1_opy_,
                         headers={bstack1l1llll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬఇ"): bstack1ll11lll1_opy_.content_type}, auth=(config[bstack1l1llll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఈ")], config[bstack1l1llll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫఉ")]))
  try:
    res = json.loads(response.text)
    bstack11l1lll11_opy_ = res[bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪఊ")]
    logger.info(bstack1111lllll_opy_.format(bstack11l1lll11_opy_))
    bstack111l1111l_opy_(md5_hash, bstack11l1lll11_opy_)
  except ValueError as err:
    bstack1111ll1_opy_(bstack11l1l1l_opy_.format(str(err)))
  return bstack11l1lll11_opy_
def bstack111ll1111_opy_():
  global CONFIG
  global bstack1l11111l1_opy_
  bstack1l1111ll1_opy_ = 0
  bstack11111l11_opy_ = 1
  if bstack1l1llll1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఋ") in CONFIG:
    bstack11111l11_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఌ")]
  if bstack1l1llll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ఍") in CONFIG:
    bstack1l1111ll1_opy_ = len(CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఎ")])
  bstack1l11111l1_opy_ = int(bstack11111l11_opy_) * int(bstack1l1111ll1_opy_)
def bstack111l1l11l_opy_(md5_hash):
  bstack1111_opy_ = os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠧࡿࠩఏ")), bstack1l1llll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨఐ"), bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ఑"))
  if os.path.exists(bstack1111_opy_):
    bstack1lll_opy_ = json.load(open(bstack1111_opy_,bstack1l1llll1l_opy_ (u"ࠪࡶࡧ࠭ఒ")))
    if md5_hash in bstack1lll_opy_:
      bstack1llll1lll_opy_ = bstack1lll_opy_[md5_hash]
      bstack1l1lll1l_opy_ = datetime.datetime.now()
      bstack1111ll1l1_opy_ = datetime.datetime.strptime(bstack1llll1lll_opy_[bstack1l1llll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఓ")], bstack1l1llll1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩఔ"))
      if (bstack1l1lll1l_opy_ - bstack1111ll1l1_opy_).days > 60:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack1llll1lll_opy_[bstack1l1llll1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫక")]):
        return None
      return bstack1llll1lll_opy_[bstack1l1llll1l_opy_ (u"ࠧࡪࡦࠪఖ")]
  else:
    return None
def bstack111l1111l_opy_(md5_hash, bstack11l1lll11_opy_):
  bstack1ll11l1_opy_ = os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠨࢀࠪగ")), bstack1l1llll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩఘ"))
  if not os.path.exists(bstack1ll11l1_opy_):
    os.makedirs(bstack1ll11l1_opy_)
  bstack1111_opy_ = os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠪࢂࠬఙ")), bstack1l1llll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫచ"), bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఛ"))
  bstack11ll1l_opy_ = {
    bstack1l1llll1l_opy_ (u"࠭ࡩࡥࠩజ"): bstack11l1lll11_opy_,
    bstack1l1llll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఝ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1llll1l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఞ")),
    bstack1l1llll1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧట"): str(__version__)
  }
  if os.path.exists(bstack1111_opy_):
    bstack1lll_opy_ = json.load(open(bstack1111_opy_,bstack1l1llll1l_opy_ (u"ࠪࡶࡧ࠭ఠ")))
  else:
    bstack1lll_opy_ = {}
  bstack1lll_opy_[md5_hash] = bstack11ll1l_opy_
  with open(bstack1111_opy_, bstack1l1llll1l_opy_ (u"ࠦࡼ࠱ࠢడ")) as outfile:
    json.dump(bstack1lll_opy_, outfile)
def bstack11l1llll_opy_(self):
  return
def bstack111l1111_opy_(self):
  return
def bstack1111l111_opy_(self):
  from selenium.webdriver.remote.webdriver import WebDriver
  WebDriver.quit(self)
def bstack1l1lllll_opy_(self):
  global bstack1l1lll11l_opy_
  global bstack1ll11_opy_
  global bstack111l_opy_
  try:
    if bstack1l1llll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬఢ") in bstack1l1lll11l_opy_ and self.session_id != None:
      bstack111ll11ll_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ణ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1llll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧత")
      bstack11l111_opy_ = bstack11ll_opy_(bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫథ"), bstack1l1llll1l_opy_ (u"ࠩࠪద"), bstack111ll11ll_opy_, bstack1l1llll1l_opy_ (u"ࠪ࠰ࠥ࠭ధ").join(threading.current_thread().bstackTestErrorMessages), bstack1l1llll1l_opy_ (u"ࠫࠬన"), bstack1l1llll1l_opy_ (u"ࠬ࠭఩"))
      if self != None:
        self.execute_script(bstack11l111_opy_)
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢప") + str(e))
  bstack111l_opy_(self)
  self.session_id = None
def bstack1lllll_opy_(self, command_executor,
        desired_capabilities=None, browser_profile=None, proxy=None,
        keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1ll11_opy_
  global bstack1l1llll_opy_
  global bstack1ll1111l_opy_
  global bstack1ll1llll_opy_
  global bstack1l1ll1111_opy_
  global bstack1l1lll11l_opy_
  global bstack11ll1lll1_opy_
  global bstack1ll1l1ll_opy_
  global bstack11l11l1l1_opy_
  CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩఫ")] = str(bstack1l1lll11l_opy_) + str(__version__)
  command_executor = bstack111ll_opy_()
  logger.debug(bstack11lll1ll1_opy_.format(command_executor))
  proxy = bstack11llll11_opy_(CONFIG, proxy)
  bstack1ll111111_opy_ = 0 if bstack1l1llll_opy_ < 0 else bstack1l1llll_opy_
  try:
    if bstack1ll1llll_opy_ is True:
      bstack1ll111111_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l1ll1111_opy_ is True:
      bstack1ll111111_opy_ = int(threading.current_thread().name)
  except:
    bstack1ll111111_opy_ = 0
  bstack1llll11ll_opy_ = bstack11ll11111_opy_(CONFIG, bstack1ll111111_opy_)
  logger.debug(bstack11l1l11ll_opy_.format(str(bstack1llll11ll_opy_)))
  if bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬబ") in CONFIG and CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭భ")]:
    bstack111llll1l_opy_(bstack1llll11ll_opy_)
  if desired_capabilities:
    bstack1l111ll_opy_ = bstack1lllllll_opy_(desired_capabilities)
    bstack1l111ll_opy_[bstack1l1llll1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪమ")] = bstack111l1l_opy_(CONFIG)
    bstack1111ll1ll_opy_ = bstack11ll11111_opy_(bstack1l111ll_opy_)
    if bstack1111ll1ll_opy_:
      bstack1llll11ll_opy_ = update(bstack1111ll1ll_opy_, bstack1llll11ll_opy_)
    desired_capabilities = None
  if options:
    bstack1l1ll11ll_opy_(options, bstack1llll11ll_opy_)
  if not options:
    options = bstack11ll11ll_opy_(bstack1llll11ll_opy_)
  if proxy and bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫయ")):
    options.proxy(proxy)
  if options and bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫర")):
    desired_capabilities = None
  if (
      not options and not desired_capabilities
  ) or (
      bstack11lll1111_opy_() < version.parse(bstack1l1llll1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬఱ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1llll11ll_opy_)
  logger.info(bstack111l1l1l_opy_)
  if bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧల")):
    bstack11ll1lll1_opy_(self, command_executor=command_executor,
          options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧళ")):
    bstack11ll1lll1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities, options=options,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  elif bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩఴ")):
    bstack11ll1lll1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11ll1lll1_opy_(self, command_executor=command_executor,
          desired_capabilities=desired_capabilities,
          browser_profile=browser_profile, proxy=proxy,
          keep_alive=keep_alive)
  try:
    bstack1ll1ll11l_opy_ = bstack1l1llll1l_opy_ (u"ࠪࠫవ")
    if bstack11lll1111_opy_() >= version.parse(bstack1l1llll1l_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬశ")):
      bstack1ll1ll11l_opy_ = self.caps.get(bstack1l1llll1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧష"))
    else:
      bstack1ll1ll11l_opy_ = self.capabilities.get(bstack1l1llll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨస"))
    if bstack1ll1ll11l_opy_:
      if bstack11lll1111_opy_() <= version.parse(bstack1l1llll1l_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧహ")):
        self.command_executor._url = bstack1l1llll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ఺") + bstack1ll1lll_opy_ + bstack1l1llll1l_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨ఻")
      else:
        self.command_executor._url = bstack1l1llll1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳఼ࠧ") + bstack1ll1ll11l_opy_ + bstack1l1llll1l_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧఽ")
      logger.debug(bstack11l11ll11_opy_.format(bstack1ll1ll11l_opy_))
    else:
      logger.debug(bstack1l1lll11_opy_.format(bstack1l1llll1l_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨా")))
  except Exception as e:
    logger.debug(bstack1l1lll11_opy_.format(e))
  if bstack1l1llll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬి") in bstack1l1lll11l_opy_:
    bstack1lll1ll1_opy_(bstack1l1llll_opy_, bstack11l11l1l1_opy_)
  bstack1ll11_opy_ = self.session_id
  if bstack1l1llll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧీ") in bstack1l1lll11l_opy_ or bstack1l1llll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨు") in bstack1l1lll11l_opy_:
    threading.current_thread().bstack111l1l1_opy_ = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1ll1l1ll_opy_.append(self)
  if bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬూ") in CONFIG and bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨృ") in CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧౄ")][bstack1ll111111_opy_]:
    bstack1ll1111l_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౅")][bstack1ll111111_opy_][bstack1l1llll1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫె")]
  logger.debug(bstack111llll11_opy_.format(bstack1ll11_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1lllll1l_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lll1l1_opy_
      if(bstack1l1llll1l_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤే") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠨࢀࠪై")), bstack1l1llll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ౉"), bstack1l1llll1l_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬొ")), bstack1l1llll1l_opy_ (u"ࠫࡼ࠭ో")) as fp:
          fp.write(bstack1l1llll1l_opy_ (u"ࠧࠨౌ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l1llll1l_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳ్ࠣ")))):
          with open(args[1], bstack1l1llll1l_opy_ (u"ࠧࡳࠩ౎")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l1llll1l_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧ౏") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1ll1l111_opy_)
            lines.insert(1, bstack11ll1l111_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l1llll1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ౐")), bstack1l1llll1l_opy_ (u"ࠪࡻࠬ౑")) as bstack111l11lll_opy_:
              bstack111l11lll_opy_.writelines(lines)
        CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭౒")] = str(bstack1l1lll11l_opy_) + str(__version__)
        bstack1ll111111_opy_ = 0 if bstack1l1llll_opy_ < 0 else bstack1l1llll_opy_
        try:
          if bstack1ll1llll_opy_ is True:
            bstack1ll111111_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l1ll1111_opy_ is True:
            bstack1ll111111_opy_ = int(threading.current_thread().name)
        except:
          bstack1ll111111_opy_ = 0
        CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧ౓")] = False
        CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ౔")] = True
        bstack1llll11ll_opy_ = bstack11ll11111_opy_(CONFIG, bstack1ll111111_opy_)
        logger.debug(bstack11l1l11ll_opy_.format(str(bstack1llll11ll_opy_)))
        if CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ౕࠫ")]:
          bstack111llll1l_opy_(bstack1llll11ll_opy_)
        if bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶౖࠫ") in CONFIG and bstack1l1llll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ౗") in CONFIG[bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ౘ")][bstack1ll111111_opy_]:
          bstack1ll1111l_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧౙ")][bstack1ll111111_opy_][bstack1l1llll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪౚ")]
        args.append(os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"࠭ࡾࠨ౛")), bstack1l1llll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ౜"), bstack1l1llll1l_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪౝ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1llll11ll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l1llll1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ౞"))
      bstack1lll1l1_opy_ = True
      return bstack11ll1ll11_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11111l1l_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1ll11_opy_
    global bstack1l1llll_opy_
    global bstack1ll1111l_opy_
    global bstack1ll1llll_opy_
    global bstack1l1ll1111_opy_
    global bstack1l1lll11l_opy_
    global bstack11ll1lll1_opy_
    CONFIG[bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ౟")] = str(bstack1l1lll11l_opy_) + str(__version__)
    bstack1ll111111_opy_ = 0 if bstack1l1llll_opy_ < 0 else bstack1l1llll_opy_
    try:
      if bstack1ll1llll_opy_ is True:
        bstack1ll111111_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l1ll1111_opy_ is True:
        bstack1ll111111_opy_ = int(threading.current_thread().name)
    except:
      bstack1ll111111_opy_ = 0
    CONFIG[bstack1l1llll1l_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥౠ")] = True
    bstack1llll11ll_opy_ = bstack11ll11111_opy_(CONFIG, bstack1ll111111_opy_)
    logger.debug(bstack11l1l11ll_opy_.format(str(bstack1llll11ll_opy_)))
    if CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩౡ")]:
      bstack111llll1l_opy_(bstack1llll11ll_opy_)
    if bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩౢ") in CONFIG and bstack1l1llll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬౣ") in CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ౤")][bstack1ll111111_opy_]:
      bstack1ll1111l_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౥")][bstack1ll111111_opy_][bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ౦")]
    import urllib
    import json
    bstack111ll1lll_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭౧") + urllib.parse.quote(json.dumps(bstack1llll11ll_opy_))
    browser = self.connect(bstack111ll1lll_opy_)
    return browser
except Exception as e:
    pass
def bstack1ll1llll1_opy_():
    global bstack1lll1l1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack11111l1l_opy_
        bstack1lll1l1_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1lllll1l_opy_
      bstack1lll1l1_opy_ = True
    except Exception as e:
      pass
def bstack1ll1l1l1l_opy_(context, bstack1ll11ll11_opy_):
  try:
    context.page.evaluate(bstack1l1llll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ౨"), bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ౩")+ json.dumps(bstack1ll11ll11_opy_) + bstack1l1llll1l_opy_ (u"ࠢࡾࡿࠥ౪"))
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨ౫"), e)
def bstack11l11llll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l1llll1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ౬"), bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ౭") + json.dumps(message) + bstack1l1llll1l_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ౮") + json.dumps(level) + bstack1l1llll1l_opy_ (u"ࠬࢃࡽࠨ౯"))
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤ౰"), e)
def bstack11_opy_(context, status, message = bstack1l1llll1l_opy_ (u"ࠢࠣ౱")):
  try:
    if(status == bstack1l1llll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ౲")):
      context.page.evaluate(bstack1l1llll1l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ౳"), bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠫ౴") + json.dumps(bstack1l1llll1l_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࠨ౵") + str(message)) + bstack1l1llll1l_opy_ (u"ࠬ࠲ࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩ౶") + json.dumps(status) + bstack1l1llll1l_opy_ (u"ࠨࡽࡾࠤ౷"))
    else:
      context.page.evaluate(bstack1l1llll1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ౸"), bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩ౹") + json.dumps(status) + bstack1l1llll1l_opy_ (u"ࠤࢀࢁࠧ౺"))
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢ౻"), e)
def bstack11l11111_opy_(self, url):
  global bstack1l11l1ll_opy_
  try:
    bstack11ll1ll1_opy_(url)
  except Exception as err:
    logger.debug(bstack111_opy_.format(str(err)))
  try:
    bstack1l11l1ll_opy_(self, url)
  except Exception as e:
    try:
      bstack1l1l1l111_opy_ = str(e)
      if any(err_msg in bstack1l1l1l111_opy_ for err_msg in bstack11ll1l1_opy_):
        bstack11ll1ll1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111_opy_.format(str(err)))
    raise e
def bstack11l111l1l_opy_(self):
  global bstack1l1l1ll1_opy_
  bstack1l1l1ll1_opy_ = self
  return
def bstack111l1ll_opy_(self):
  global bstack11l1l1l1l_opy_
  bstack11l1l1l1l_opy_ = self
  return
def bstack111ll1l_opy_(self, test):
  global CONFIG
  global bstack11l1l1l1l_opy_
  global bstack1l1l1ll1_opy_
  global bstack1ll11_opy_
  global bstack1l1ll1ll_opy_
  global bstack1ll1111l_opy_
  global bstack1l1l11ll1_opy_
  global bstack11ll1lll_opy_
  global bstack1l1lll1l1_opy_
  global bstack1ll1l1ll_opy_
  try:
    if not bstack1ll11_opy_:
      with open(os.path.join(os.path.expanduser(bstack1l1llll1l_opy_ (u"ࠫࢃ࠭౼")), bstack1l1llll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ౽"), bstack1l1llll1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨ౾"))) as f:
        bstack1llll11l1_opy_ = json.loads(bstack1l1llll1l_opy_ (u"ࠢࡼࠤ౿") + f.read().strip() + bstack1l1llll1l_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪಀ") + bstack1l1llll1l_opy_ (u"ࠤࢀࠦಁ"))
        bstack1ll11_opy_ = bstack1llll11l1_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1ll1l1ll_opy_:
    for driver in bstack1ll1l1ll_opy_:
      if bstack1ll11_opy_ == driver.session_id:
        if test:
          bstack111l111ll_opy_ = str(test.data)
        if not bstack1ll111l1l_opy_ and bstack111l111ll_opy_:
          bstack1ll1l11_opy_ = {
            bstack1l1llll1l_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪಂ"): bstack1l1llll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಃ"),
            bstack1l1llll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ಄"): {
              bstack1l1llll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫಅ"): bstack111l111ll_opy_
            }
          }
          bstack11lll11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬಆ").format(json.dumps(bstack1ll1l11_opy_))
          driver.execute_script(bstack11lll11l1_opy_)
        if bstack1l1ll1ll_opy_:
          bstack11llll1_opy_ = {
            bstack1l1llll1l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨಇ"): bstack1l1llll1l_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫಈ"),
            bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ಉ"): {
              bstack1l1llll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩಊ"): bstack111l111ll_opy_ + bstack1l1llll1l_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧಋ"),
              bstack1l1llll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬಌ"): bstack1l1llll1l_opy_ (u"ࠧࡪࡰࡩࡳࠬ಍")
            }
          }
          bstack1ll1l11_opy_ = {
            bstack1l1llll1l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨಎ"): bstack1l1llll1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬಏ"),
            bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ಐ"): {
              bstack1l1llll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ಑"): bstack1l1llll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬಒ")
            }
          }
          if bstack1l1ll1ll_opy_.status == bstack1l1llll1l_opy_ (u"࠭ࡐࡂࡕࡖࠫಓ"):
            bstack11ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬಔ").format(json.dumps(bstack11llll1_opy_))
            driver.execute_script(bstack11ll1_opy_)
            bstack11lll11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ಕ").format(json.dumps(bstack1ll1l11_opy_))
            driver.execute_script(bstack11lll11l1_opy_)
          elif bstack1l1ll1ll_opy_.status == bstack1l1llll1l_opy_ (u"ࠩࡉࡅࡎࡒࠧಖ"):
            reason = bstack1l1llll1l_opy_ (u"ࠥࠦಗ")
            bstack1lll11l11_opy_ = bstack111l111ll_opy_ + bstack1l1llll1l_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠬಘ")
            if bstack1l1ll1ll_opy_.message:
              reason = str(bstack1l1ll1ll_opy_.message)
              bstack1lll11l11_opy_ = bstack1lll11l11_opy_ + bstack1l1llll1l_opy_ (u"ࠬࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࠬಙ") + reason
            bstack11llll1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩಚ")] = {
              bstack1l1llll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ಛ"): bstack1l1llll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧಜ"),
              bstack1l1llll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧಝ"): bstack1lll11l11_opy_
            }
            bstack1ll1l11_opy_[bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ಞ")] = {
              bstack1l1llll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫಟ"): bstack1l1llll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬಠ"),
              bstack1l1llll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ಡ"): reason
            }
            bstack11ll1_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬಢ").format(json.dumps(bstack11llll1_opy_))
            driver.execute_script(bstack11ll1_opy_)
            bstack11lll11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ಣ").format(json.dumps(bstack1ll1l11_opy_))
            driver.execute_script(bstack11lll11l1_opy_)
  elif bstack1ll11_opy_:
    try:
      data = {}
      bstack111l111ll_opy_ = None
      if test:
        bstack111l111ll_opy_ = str(test.data)
      if not bstack1ll111l1l_opy_ and bstack111l111ll_opy_:
        data[bstack1l1llll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧತ")] = bstack111l111ll_opy_
      if bstack1l1ll1ll_opy_:
        if bstack1l1ll1ll_opy_.status == bstack1l1llll1l_opy_ (u"ࠪࡔࡆ࡙ࡓࠨಥ"):
          data[bstack1l1llll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫದ")] = bstack1l1llll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬಧ")
        elif bstack1l1ll1ll_opy_.status == bstack1l1llll1l_opy_ (u"࠭ࡆࡂࡋࡏࠫನ"):
          data[bstack1l1llll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ಩")] = bstack1l1llll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨಪ")
          if bstack1l1ll1ll_opy_.message:
            data[bstack1l1llll1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩಫ")] = str(bstack1l1ll1ll_opy_.message)
      user = CONFIG[bstack1l1llll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬಬ")]
      key = CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧಭ")]
      url = bstack1l1llll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠱ࡾࢁ࠳ࡰࡳࡰࡰࠪಮ").format(user, key, bstack1ll11_opy_)
      headers = {
        bstack1l1llll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬಯ"): bstack1l1llll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪರ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll11ll1l_opy_.format(str(e)))
  if bstack11l1l1l1l_opy_:
    bstack11ll1lll_opy_(bstack11l1l1l1l_opy_)
  if bstack1l1l1ll1_opy_:
    bstack1l1lll1l1_opy_(bstack1l1l1ll1_opy_)
  bstack1l1l11ll1_opy_(self, test)
def bstack1ll111lll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l11l_opy_
  bstack1l11l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l1ll1ll_opy_
  bstack1l1ll1ll_opy_ = self._test
def bstack1ll1ll_opy_():
  global bstack11l1lllll_opy_
  try:
    if os.path.exists(bstack11l1lllll_opy_):
      os.remove(bstack11l1lllll_opy_)
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫಱ") + str(e))
def bstack111ll1ll1_opy_():
  global bstack11l1lllll_opy_
  bstack1l11l1l1_opy_ = {}
  try:
    if not os.path.isfile(bstack11l1lllll_opy_):
      with open(bstack11l1lllll_opy_, bstack1l1llll1l_opy_ (u"ࠩࡺࠫಲ")):
        pass
      with open(bstack11l1lllll_opy_, bstack1l1llll1l_opy_ (u"ࠥࡻ࠰ࠨಳ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack11l1lllll_opy_):
      bstack1l11l1l1_opy_ = json.load(open(bstack11l1lllll_opy_, bstack1l1llll1l_opy_ (u"ࠫࡷࡨࠧ಴")))
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧವ") + str(e))
  finally:
    return bstack1l11l1l1_opy_
def bstack1lll1ll1_opy_(platform_index, item_index):
  global bstack11l1lllll_opy_
  try:
    bstack1l11l1l1_opy_ = bstack111ll1ll1_opy_()
    bstack1l11l1l1_opy_[item_index] = platform_index
    with open(bstack11l1lllll_opy_, bstack1l1llll1l_opy_ (u"ࠨࡷࠬࠤಶ")) as outfile:
      json.dump(bstack1l11l1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡸࡴࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬಷ") + str(e))
def bstack1l1111lll_opy_(bstack1l11ll1l_opy_):
  global CONFIG
  bstack1l1111l11_opy_ = bstack1l1llll1l_opy_ (u"ࠨࠩಸ")
  if not bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಹ") in CONFIG:
    logger.info(bstack1l1llll1l_opy_ (u"ࠪࡒࡴࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠢࡳࡥࡸࡹࡥࡥࠢࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡳࡧࡳࡳࡷࡺࠠࡧࡱࡵࠤࡗࡵࡢࡰࡶࠣࡶࡺࡴࠧ಺"))
  try:
    platform = CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಻")][bstack1l11ll1l_opy_]
    if bstack1l1llll1l_opy_ (u"ࠬࡵࡳࠨ಼") in platform:
      bstack1l1111l11_opy_ += str(platform[bstack1l1llll1l_opy_ (u"࠭࡯ࡴࠩಽ")]) + bstack1l1llll1l_opy_ (u"ࠧ࠭ࠢࠪಾ")
    if bstack1l1llll1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫಿ") in platform:
      bstack1l1111l11_opy_ += str(platform[bstack1l1llll1l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬೀ")]) + bstack1l1llll1l_opy_ (u"ࠪ࠰ࠥ࠭ು")
    if bstack1l1llll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨೂ") in platform:
      bstack1l1111l11_opy_ += str(platform[bstack1l1llll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩೃ")]) + bstack1l1llll1l_opy_ (u"࠭ࠬࠡࠩೄ")
    if bstack1l1llll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ೅") in platform:
      bstack1l1111l11_opy_ += str(platform[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪೆ")]) + bstack1l1llll1l_opy_ (u"ࠩ࠯ࠤࠬೇ")
    if bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨೈ") in platform:
      bstack1l1111l11_opy_ += str(platform[bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ೉")]) + bstack1l1llll1l_opy_ (u"ࠬ࠲ࠠࠨೊ")
    if bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧೋ") in platform:
      bstack1l1111l11_opy_ += str(platform[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨೌ")]) + bstack1l1llll1l_opy_ (u"ࠨ࠮್ࠣࠫ")
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠩࡖࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡵࡷࡶ࡮ࡴࡧࠡࡨࡲࡶࠥࡸࡥࡱࡱࡵࡸࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡯࡯ࠩ೎") + str(e))
  finally:
    if bstack1l1111l11_opy_[len(bstack1l1111l11_opy_) - 2:] == bstack1l1llll1l_opy_ (u"ࠪ࠰ࠥ࠭೏"):
      bstack1l1111l11_opy_ = bstack1l1111l11_opy_[:-2]
    return bstack1l1111l11_opy_
def bstack1ll1lll1_opy_(path, bstack1l1111l11_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11ll11l1_opy_ = ET.parse(path)
    bstack1l1111l1_opy_ = bstack11ll11l1_opy_.getroot()
    bstack1l1lll_opy_ = None
    for suite in bstack1l1111l1_opy_.iter(bstack1l1llll1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ೐")):
      if bstack1l1llll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ೑") in suite.attrib:
        suite.attrib[bstack1l1llll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೒")] += bstack1l1llll1l_opy_ (u"ࠧࠡࠩ೓") + bstack1l1111l11_opy_
        bstack1l1lll_opy_ = suite
    bstack1ll1lllll_opy_ = None
    for robot in bstack1l1111l1_opy_.iter(bstack1l1llll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ೔")):
      bstack1ll1lllll_opy_ = robot
    bstack1lll1l111_opy_ = len(bstack1ll1lllll_opy_.findall(bstack1l1llll1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨೕ")))
    if bstack1lll1l111_opy_ == 1:
      bstack1ll1lllll_opy_.remove(bstack1ll1lllll_opy_.findall(bstack1l1llll1l_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩೖ"))[0])
      bstack11l11l_opy_ = ET.Element(bstack1l1llll1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ೗"), attrib={bstack1l1llll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೘"):bstack1l1llll1l_opy_ (u"࠭ࡓࡶ࡫ࡷࡩࡸ࠭೙"), bstack1l1llll1l_opy_ (u"ࠧࡪࡦࠪ೚"):bstack1l1llll1l_opy_ (u"ࠨࡵ࠳ࠫ೛")})
      bstack1ll1lllll_opy_.insert(1, bstack11l11l_opy_)
      bstack1l11lllll_opy_ = None
      for suite in bstack1ll1lllll_opy_.iter(bstack1l1llll1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ೜")):
        bstack1l11lllll_opy_ = suite
      bstack1l11lllll_opy_.append(bstack1l1lll_opy_)
      bstack1ll111l_opy_ = None
      for status in bstack1l1lll_opy_.iter(bstack1l1llll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪೝ")):
        bstack1ll111l_opy_ = status
      bstack1l11lllll_opy_.append(bstack1ll111l_opy_)
    bstack11ll11l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠩೞ") + str(e))
def bstack1l1l111l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l11l111l_opy_
  global CONFIG
  if bstack1l1llll1l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤ೟") in options:
    del options[bstack1l1llll1l_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡶࡡࡵࡪࠥೠ")]
  bstack1l1ll11_opy_ = bstack111ll1ll1_opy_()
  for bstack1l1l1ll1l_opy_ in bstack1l1ll11_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1l1llll1l_opy_ (u"ࠧࡱࡣࡥࡳࡹࡥࡲࡦࡵࡸࡰࡹࡹࠧೡ"), str(bstack1l1l1ll1l_opy_), bstack1l1llll1l_opy_ (u"ࠨࡱࡸࡸࡵࡻࡴ࠯ࡺࡰࡰࠬೢ"))
    bstack1ll1lll1_opy_(path, bstack1l1111lll_opy_(bstack1l1ll11_opy_[bstack1l1l1ll1l_opy_]))
  bstack1ll1ll_opy_()
  return bstack1l11l111l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11111_opy_(self, ff_profile_dir):
  global bstack1l1l111_opy_
  if not ff_profile_dir:
    return None
  return bstack1l1l111_opy_(self, ff_profile_dir)
def bstack1l11l11l1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack11l1l111_opy_
  bstack11l111l_opy_ = []
  if bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೣ") in CONFIG:
    bstack11l111l_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೤")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l1llll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࠧ೥")],
      pabot_args[bstack1l1llll1l_opy_ (u"ࠧࡼࡥࡳࡤࡲࡷࡪࠨ೦")],
      argfile,
      pabot_args.get(bstack1l1llll1l_opy_ (u"ࠨࡨࡪࡸࡨࠦ೧")),
      pabot_args[bstack1l1llll1l_opy_ (u"ࠢࡱࡴࡲࡧࡪࡹࡳࡦࡵࠥ೨")],
      platform[0],
      bstack11l1l111_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l1llll1l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡩ࡭ࡱ࡫ࡳࠣ೩")] or [(bstack1l1llll1l_opy_ (u"ࠤࠥ೪"), None)]
    for platform in enumerate(bstack11l111l_opy_)
  ]
def bstack1l111_opy_(self, datasources, outs_dir, options,
  execution_item, command, verbose, argfile,
  hive=None, processes=0,platform_index=0,bstack1lll111l_opy_=bstack1l1llll1l_opy_ (u"ࠪࠫ೫")):
  global bstack11lll111l_opy_
  self.platform_index = platform_index
  self.bstack1l1l1ll11_opy_ = bstack1lll111l_opy_
  bstack11lll111l_opy_(self, datasources, outs_dir, options,
    execution_item, command, verbose, argfile, hive, processes)
def bstack1ll111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll111l11_opy_
  global bstack11l1l1lll_opy_
  if not bstack1l1llll1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭೬") in item.options:
    item.options[bstack1l1llll1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ೭")] = []
  for v in item.options[bstack1l1llll1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ೮")]:
    if bstack1l1llll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭೯") in v:
      item.options[bstack1l1llll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ೰")].remove(v)
    if bstack1l1llll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔࠩೱ") in v:
      item.options[bstack1l1llll1l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬೲ")].remove(v)
  item.options[bstack1l1llll1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ೳ")].insert(0, bstack1l1llll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛࠾ࢀࢃࠧ೴").format(item.platform_index))
  item.options[bstack1l1llll1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ೵")].insert(0, bstack1l1llll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࢀࢃࠧ೶").format(item.bstack1l1l1ll11_opy_))
  if bstack11l1l1lll_opy_:
    item.options[bstack1l1llll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ೷")].insert(0, bstack1l1llll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔ࠼ࡾࢁࠬ೸").format(bstack11l1l1lll_opy_))
  return bstack1ll111l11_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack11lll1lll_opy_(command, item_index):
  global bstack11l1l1lll_opy_
  if bstack11l1l1lll_opy_:
    command[0] = command[0].replace(bstack1l1llll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ೹"), bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨ೺") + str(item_index) + bstack1l1llll1l_opy_ (u"ࠬࠦࠧ೻") + bstack11l1l1lll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack1l1llll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ೼"), bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫ೽") + str(item_index), 1)
def bstack1l11l1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11ll1l11l_opy_
  bstack11lll1lll_opy_(command, item_index)
  return bstack11ll1l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack1l1ll1ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11ll1l11l_opy_
  bstack11lll1lll_opy_(command, item_index)
  return bstack11ll1l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack1ll11l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11ll1l11l_opy_
  bstack11lll1lll_opy_(command, item_index)
  return bstack11ll1l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1111ll11l_opy_(self, runner, quiet=False, capture=True):
  global bstack11l1llll1_opy_
  bstack1lll11l1l_opy_ = bstack11l1llll1_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack1l1llll1l_opy_ (u"ࠨࡧࡻࡧࡪࡶࡴࡪࡱࡱࡣࡦࡸࡲࠨ೾")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l1llll1l_opy_ (u"ࠩࡨࡼࡨࡥࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࡡࡤࡶࡷ࠭೿")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1lll11l1l_opy_
def bstack11l1111l1_opy_(self, name, context, *args):
  global bstack1l1l1l_opy_
  if name == bstack1l1llll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠫഀ"):
    bstack1l1l1l_opy_(self, name, context, *args)
    try:
      if(not bstack1ll111l1l_opy_):
        bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11ll11l_opy_(bstack1l1llll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪഁ")) else context.browser
        bstack1ll11ll11_opy_ = str(self.feature.name)
        bstack1ll1l1l1l_opy_(context, bstack1ll11ll11_opy_)
        bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪം") + json.dumps(bstack1ll11ll11_opy_) + bstack1l1llll1l_opy_ (u"࠭ࡽࡾࠩഃ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack1l1llll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧഄ").format(str(e)))
  elif name == bstack1l1llll1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪഅ"):
    bstack1l1l1l_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack1l1llll1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫആ")):
        self.driver_before_scenario = True
      if(not bstack1ll111l1l_opy_):
        scenario_name = args[0].name
        feature_name = bstack1ll11ll11_opy_ = str(self.feature.name)
        bstack1ll11ll11_opy_ = feature_name + bstack1l1llll1l_opy_ (u"ࠪࠤ࠲ࠦࠧഇ") + scenario_name
        bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11ll11l_opy_(bstack1l1llll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪഈ")) else context.browser
        if self.driver_before_scenario:
          bstack1ll1l1l1l_opy_(context, bstack1ll11ll11_opy_)
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪഉ") + json.dumps(bstack1ll11ll11_opy_) + bstack1l1llll1l_opy_ (u"࠭ࡽࡾࠩഊ"))
    except Exception as e:
      logger.debug(bstack1l1llll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨഋ").format(str(e)))
  elif name == bstack1l1llll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩഌ"):
    try:
      bstack11111l_opy_ = args[0].status.name
      bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1llll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ഍") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack11111l_opy_).lower() == bstack1l1llll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪഎ"):
        bstack1lllll1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠫࠬഏ")
        bstack1ll1l1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠬ࠭ഐ")
        bstack1ll1lll1l_opy_ = bstack1l1llll1l_opy_ (u"࠭ࠧ഑")
        try:
          import traceback
          bstack1lllll1l1_opy_ = self.exception.__class__.__name__
          bstack111l11l_opy_ = traceback.format_tb(self.exc_traceback)
          bstack1ll1l1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠧࠡࠩഒ").join(bstack111l11l_opy_)
          bstack1ll1lll1l_opy_ = bstack111l11l_opy_[-1]
        except Exception as e:
          logger.debug(bstack1l1l_opy_.format(str(e)))
        bstack1lllll1l1_opy_ += bstack1ll1lll1l_opy_
        bstack11l11llll_opy_(context, json.dumps(str(args[0].name) + bstack1l1llll1l_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢഓ") + str(bstack1ll1l1l1_opy_)), bstack1l1llll1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣഔ"))
        if self.driver_before_scenario:
          bstack11_opy_(context, bstack1l1llll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥക"), bstack1lllll1l1_opy_)
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩഖ") + json.dumps(str(args[0].name) + bstack1l1llll1l_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦഗ") + str(bstack1ll1l1l1_opy_)) + bstack1l1llll1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ഘ"))
        if self.driver_before_scenario:
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࠮ࠣࠦࡷ࡫ࡡࡴࡱࡱࠦ࠿ࠦࠧങ") + json.dumps(bstack1l1llll1l_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧച") + str(bstack1lllll1l1_opy_)) + bstack1l1llll1l_opy_ (u"ࠩࢀࢁࠬഛ"))
      else:
        bstack11l11llll_opy_(context, bstack1l1llll1l_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦജ"), bstack1l1llll1l_opy_ (u"ࠦ࡮ࡴࡦࡰࠤഝ"))
        if self.driver_before_scenario:
          bstack11_opy_(context, bstack1l1llll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧഞ"))
        bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫട") + json.dumps(str(args[0].name) + bstack1l1llll1l_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦഠ")) + bstack1l1llll1l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧഡ"))
        if self.driver_before_scenario:
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡵࡷࡥࡹࡻࡳࠣ࠼ࠥࡴࡦࡹࡳࡦࡦࠥࢁࢂ࠭ഢ"))
    except Exception as e:
      logger.debug(bstack1l1llll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬണ").format(str(e)))
  elif name == bstack1l1llll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫത"):
    try:
      bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11ll11l_opy_(bstack1l1llll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫഥ")) else context.browser
      if context.failed is True:
        bstack11l11l1l_opy_ = []
        bstack1lllll1ll_opy_ = []
        bstack1lll111_opy_ = []
        bstack1l111llll_opy_ = bstack1l1llll1l_opy_ (u"࠭ࠧദ")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack11l11l1l_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack111l11l_opy_ = traceback.format_tb(exc_tb)
            bstack1l1l11ll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࠡࠩധ").join(bstack111l11l_opy_)
            bstack1lllll1ll_opy_.append(bstack1l1l11ll_opy_)
            bstack1lll111_opy_.append(bstack111l11l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1l_opy_.format(str(e)))
        bstack1lllll1l1_opy_ = bstack1l1llll1l_opy_ (u"ࠨࠩന")
        for i in range(len(bstack11l11l1l_opy_)):
          bstack1lllll1l1_opy_ += bstack11l11l1l_opy_[i] + bstack1lll111_opy_[i] + bstack1l1llll1l_opy_ (u"ࠩ࡟ࡲࠬഩ")
        bstack1l111llll_opy_ = bstack1l1llll1l_opy_ (u"ࠪࠤࠬപ").join(bstack1lllll1ll_opy_)
        if not self.driver_before_scenario:
          bstack11l11llll_opy_(context, bstack1l111llll_opy_, bstack1l1llll1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥഫ"))
          bstack11_opy_(context, bstack1l1llll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧബ"), bstack1lllll1l1_opy_)
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫഭ") + json.dumps(bstack1l111llll_opy_) + bstack1l1llll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧമ"))
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠤࡩࡥ࡮ࡲࡥࡥࠤ࠯ࠤࠧࡸࡥࡢࡵࡲࡲࠧࡀࠠࠨയ") + json.dumps(bstack1l1llll1l_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢര") + str(bstack1lllll1l1_opy_)) + bstack1l1llll1l_opy_ (u"ࠪࢁࢂ࠭റ"))
      else:
        if not self.driver_before_scenario:
          bstack11l11llll_opy_(context, bstack1l1llll1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢല") + str(self.feature.name) + bstack1l1llll1l_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢള"), bstack1l1llll1l_opy_ (u"ࠨࡩ࡯ࡨࡲࠦഴ"))
          bstack11_opy_(context, bstack1l1llll1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢവ"))
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ശ") + json.dumps(bstack1l1llll1l_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧഷ") + str(self.feature.name) + bstack1l1llll1l_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧസ")) + bstack1l1llll1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪഹ"))
          bstack111l1lll1_opy_.execute_script(bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡸࡺࡡࡵࡷࡶࠦ࠿ࠨࡰࡢࡵࡶࡩࡩࠨࡽࡾࠩഺ"))
    except Exception as e:
      logger.debug(bstack1l1llll1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ഻").format(str(e)))
  else:
    bstack1l1l1l_opy_(self, name, context, *args)
  if name in [bstack1l1llll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫഼ࠧ"), bstack1l1llll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩഽ")]:
    bstack1l1l1l_opy_(self, name, context, *args)
    if (name == bstack1l1llll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪാ") and self.driver_before_scenario) or (name == bstack1l1llll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪി") and not self.driver_before_scenario):
      try:
        bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11ll11l_opy_(bstack1l1llll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪീ")) else context.browser
        bstack111l1lll1_opy_.quit()
      except Exception:
        pass
def bstack1l1111l_opy_(config, startdir):
  return bstack1l1llll1l_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࠱ࡿࠥു").format(bstack1l1llll1l_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧൂ"))
class Notset:
  def __repr__(self):
    return bstack1l1llll1l_opy_ (u"ࠢ࠽ࡐࡒࡘࡘࡋࡔ࠿ࠤൃ")
notset = Notset()
def bstack1lll1111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1lll1111_opy_
  if str(name).lower() == bstack1l1llll1l_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨൄ"):
    return bstack1l1llll1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣ൅")
  else:
    return bstack1lll1111_opy_(self, name, default, skip)
def bstack1l1l1_opy_(item, when):
  global bstack11llll_opy_
  try:
    bstack11llll_opy_(item, when)
  except Exception as e:
    pass
def bstack1lll111ll_opy_():
  return
def bstack11ll_opy_(type, name, status, reason, bstack1lllll11_opy_, bstack11lll1l1_opy_):
  bstack1ll1l11_opy_ = {
    bstack1l1llll1l_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪെ"): type,
    bstack1l1llll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧേ"): {}
  }
  if type == bstack1l1llll1l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧൈ"):
    bstack1ll1l11_opy_[bstack1l1llll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ൉")][bstack1l1llll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ൊ")] = bstack1lllll11_opy_
    bstack1ll1l11_opy_[bstack1l1llll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫോ")][bstack1l1llll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧൌ")] = json.dumps(str(bstack11lll1l1_opy_))
  if type == bstack1l1llll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨ്ࠫ"):
    bstack1ll1l11_opy_[bstack1l1llll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧൎ")][bstack1l1llll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ൏")] = name
  if type == bstack1l1llll1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ൐"):
    bstack1ll1l11_opy_[bstack1l1llll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ൑")][bstack1l1llll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ൒")] = status
    if status == bstack1l1llll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ൓"):
      bstack1ll1l11_opy_[bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ൔ")][bstack1l1llll1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫൕ")] = json.dumps(str(reason))
  bstack11lll11l1_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪൖ").format(json.dumps(bstack1ll1l11_opy_))
  return bstack11lll11l1_opy_
def bstack111lll1l_opy_(item, call, rep):
  global bstack11l11ll1l_opy_
  global bstack1ll1l1ll_opy_
  name = bstack1l1llll1l_opy_ (u"࠭ࠧൗ")
  try:
    if rep.when == bstack1l1llll1l_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ൘"):
      bstack1ll11_opy_ = threading.current_thread().bstack111l1l1_opy_
      try:
        name = str(rep.nodeid)
        bstack11l111_opy_ = bstack11ll_opy_(bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ൙"), name, bstack1l1llll1l_opy_ (u"ࠩࠪ൚"), bstack1l1llll1l_opy_ (u"ࠪࠫ൛"), bstack1l1llll1l_opy_ (u"ࠫࠬ൜"), bstack1l1llll1l_opy_ (u"ࠬ࠭൝"))
        for driver in bstack1ll1l1ll_opy_:
          if bstack1ll11_opy_ == driver.session_id:
            driver.execute_script(bstack11l111_opy_)
      except Exception as e:
        logger.debug(bstack1l1llll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭൞").format(str(e)))
      try:
        status = bstack1l1llll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧൟ") if rep.outcome.lower() == bstack1l1llll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨൠ") else bstack1l1llll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩൡ")
        reason = bstack1l1llll1l_opy_ (u"ࠪࠫൢ")
        if (reason != bstack1l1llll1l_opy_ (u"ࠦࠧൣ")):
          try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
          except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
          threading.current_thread().bstackTestErrorMessages.append(str(reason))
        if status == bstack1l1llll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ൤"):
          reason = rep.longrepr.reprcrash.message
          if (not threading.current_thread().bstackTestErrorMessages):
            threading.current_thread().bstackTestErrorMessages = []
          threading.current_thread().bstackTestErrorMessages.append(reason)
        level = bstack1l1llll1l_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ൥") if status == bstack1l1llll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ൦") else bstack1l1llll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ൧")
        data = name + bstack1l1llll1l_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ൨") if status == bstack1l1llll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ൩") else name + bstack1l1llll1l_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧ൪") + reason
        bstack11ll111ll_opy_ = bstack11ll_opy_(bstack1l1llll1l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ൫"), bstack1l1llll1l_opy_ (u"࠭ࠧ൬"), bstack1l1llll1l_opy_ (u"ࠧࠨ൭"), bstack1l1llll1l_opy_ (u"ࠨࠩ൮"), level, data)
        for driver in bstack1ll1l1ll_opy_:
          if bstack1ll11_opy_ == driver.session_id:
            driver.execute_script(bstack11ll111ll_opy_)
      except Exception as e:
        logger.debug(bstack1l1llll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭൯").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l1llll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧ൰").format(str(e)))
  bstack11l11ll1l_opy_(item, call, rep)
def bstack1ll1ll1l_opy_(framework_name):
  global bstack1l1lll11l_opy_
  global bstack1lll1l1_opy_
  global bstack111ll1l1_opy_
  bstack1l1lll11l_opy_ = framework_name
  logger.info(bstack1lll1ll11_opy_.format(bstack1l1lll11l_opy_.split(bstack1l1llll1l_opy_ (u"ࠫ࠲࠭൱"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    Service.start = bstack11l1llll_opy_
    Service.stop = bstack111l1111_opy_
    webdriver.Remote.__init__ = bstack1lllll_opy_
    webdriver.Remote.get = bstack11l11111_opy_
    WebDriver.close = bstack1111l111_opy_
    WebDriver.quit = bstack1l1lllll_opy_
    bstack1lll1l1_opy_ = True
  except Exception as e:
    pass
  bstack1ll1llll1_opy_()
  if not bstack1lll1l1_opy_:
    bstack1ll1l1l_opy_(bstack1l1llll1l_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢ൲"), bstack111lll11l_opy_)
  if bstack11llll1l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack11l1l1_opy_
    except Exception as e:
      logger.error(bstack1l1l1l1ll_opy_.format(str(e)))
  if (bstack1l1llll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൳") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack111l1ll_opy_
      except Exception as e:
        logger.warn(bstack1ll11l1l1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11l111l1l_opy_
      except Exception as e:
        logger.debug(bstack1ll11ll1_opy_ + str(e))
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1ll11l1l1_opy_)
    Output.end_test = bstack111ll1l_opy_
    TestStatus.__init__ = bstack1ll111lll_opy_
    QueueItem.__init__ = bstack1l111_opy_
    pabot._create_items = bstack1l11l11l1_opy_
    try:
      from pabot import __version__ as bstack11111l1_opy_
      if version.parse(bstack11111l1_opy_) >= version.parse(bstack1l1llll1l_opy_ (u"ࠧ࠳࠰࠴࠹࠳࠶ࠧ൴")):
        pabot._run = bstack1ll11l11l_opy_
      elif version.parse(bstack11111l1_opy_) >= version.parse(bstack1l1llll1l_opy_ (u"ࠨ࠴࠱࠵࠸࠴࠰ࠨ൵")):
        pabot._run = bstack1l1ll1ll1_opy_
      else:
        pabot._run = bstack1l11l1111_opy_
    except Exception as e:
      pabot._run = bstack1l11l1111_opy_
    pabot._create_command_for_execution = bstack1ll111_opy_
    pabot._report_results = bstack1l1l111l1_opy_
  if bstack1l1llll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ൶") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1l11l111_opy_)
    Runner.run_hook = bstack11l1111l1_opy_
    Step.run = bstack1111ll11l_opy_
  if bstack1l1llll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ൷") in str(framework_name).lower():
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l1111l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1lll111ll_opy_
      Config.getoption = bstack1lll1111l_opy_
    except Exception as e:
      pass
    try:
      from _pytest import runner
      runner._update_current_test_var = bstack1l1l1_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111lll1l_opy_
    except Exception as e:
      pass
def bstack11111ll_opy_():
  global CONFIG
  if bstack1l1llll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ൸") in CONFIG and int(CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ൹")]) > 1:
    logger.warn(bstack1lll11ll_opy_)
def bstack111l1l1ll_opy_(arg):
  arg.append(bstack1l1llll1l_opy_ (u"ࠨ࠭࠮࡫ࡰࡴࡴࡸࡴ࠮࡯ࡲࡨࡪࡃࡩ࡮ࡲࡲࡶࡹࡲࡩࡣࠤൺ"))
  arg.append(bstack1l1llll1l_opy_ (u"ࠢ࠮࡙ࠥൻ"))
  arg.append(bstack1l1llll1l_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡏࡲࡨࡺࡲࡥࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡱࡵࡵࡲࡵࡧࡧ࠾ࡵࡿࡴࡦࡵࡷ࠲ࡕࡿࡴࡦࡵࡷ࡛ࡦࡸ࡮ࡪࡰࡪࠦർ"))
  arg.append(bstack1l1llll1l_opy_ (u"ࠤ࠰࡛ࠧൽ"))
  arg.append(bstack1l1llll1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡘ࡭࡫ࠠࡩࡱࡲ࡯࡮ࡳࡰ࡭ࠤൾ"))
  global CONFIG
  bstack1ll1ll1l_opy_(bstack1l1ll1l11_opy_)
  os.environ[bstack1l1llll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬൿ")] = CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ඀")]
  os.environ[bstack1l1llll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩඁ")] = CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪං")]
  from _pytest.config import main as bstack11l1l11_opy_
  bstack11l1l11_opy_(arg)
def bstack11ll111l_opy_(arg):
  bstack1ll1ll1l_opy_(bstack1lll11l1_opy_)
  from behave.__main__ import main as bstack11l111lll_opy_
  bstack11l111lll_opy_(arg)
def bstack11111lll_opy_():
  logger.info(bstack1ll1ll1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧඃ"), help=bstack1l1llll1l_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡴࡴࡦࡪࡩࠪ඄"))
  parser.add_argument(bstack1l1llll1l_opy_ (u"ࠪ࠱ࡺ࠭අ"), bstack1l1llll1l_opy_ (u"ࠫ࠲࠳ࡵࡴࡧࡵࡲࡦࡳࡥࠨආ"), help=bstack1l1llll1l_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫඇ"))
  parser.add_argument(bstack1l1llll1l_opy_ (u"࠭࠭࡬ࠩඈ"), bstack1l1llll1l_opy_ (u"ࠧ࠮࠯࡮ࡩࡾ࠭ඉ"), help=bstack1l1llll1l_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠩඊ"))
  parser.add_argument(bstack1l1llll1l_opy_ (u"ࠩ࠰ࡪࠬඋ"), bstack1l1llll1l_opy_ (u"ࠪ࠱࠲࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨඌ"), help=bstack1l1llll1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪඍ"))
  bstack1ll1l1lll_opy_ = parser.parse_args()
  try:
    bstack1llll1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡮ࡦࡴ࡬ࡧ࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩඎ")
    if bstack1ll1l1lll_opy_.framework and bstack1ll1l1lll_opy_.framework not in (bstack1l1llll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ඏ"), bstack1l1llll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨඐ")):
      bstack1llll1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧඑ")
    bstack1l111ll1l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1llll1l11_opy_)
    bstack111l1ll1_opy_ = open(bstack1l111ll1l_opy_, bstack1l1llll1l_opy_ (u"ࠩࡵࠫඒ"))
    bstack11ll1l1l_opy_ = bstack111l1ll1_opy_.read()
    bstack111l1ll1_opy_.close()
    if bstack1ll1l1lll_opy_.username:
      bstack11ll1l1l_opy_ = bstack11ll1l1l_opy_.replace(bstack1l1llll1l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪඓ"), bstack1ll1l1lll_opy_.username)
    if bstack1ll1l1lll_opy_.key:
      bstack11ll1l1l_opy_ = bstack11ll1l1l_opy_.replace(bstack1l1llll1l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ඔ"), bstack1ll1l1lll_opy_.key)
    if bstack1ll1l1lll_opy_.framework:
      bstack11ll1l1l_opy_ = bstack11ll1l1l_opy_.replace(bstack1l1llll1l_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ඕ"), bstack1ll1l1lll_opy_.framework)
    file_name = bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩඖ")
    file_path = os.path.abspath(file_name)
    bstack11llll1ll_opy_ = open(file_path, bstack1l1llll1l_opy_ (u"ࠧࡸࠩ඗"))
    bstack11llll1ll_opy_.write(bstack11ll1l1l_opy_)
    bstack11llll1ll_opy_.close()
    logger.info(bstack1l1l1lll1_opy_)
    try:
      os.environ[bstack1l1llll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ඘")] = bstack1ll1l1lll_opy_.framework if bstack1ll1l1lll_opy_.framework != None else bstack1l1llll1l_opy_ (u"ࠤࠥ඙")
      config = yaml.safe_load(bstack11ll1l1l_opy_)
      config[bstack1l1llll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪක")] = bstack1l1llll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡸ࡫ࡴࡶࡲࠪඛ")
      bstack1l1l1l11l_opy_(bstack111lll11_opy_, config)
    except Exception as e:
      logger.debug(bstack11ll11l11_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll1ll111_opy_.format(str(e)))
def bstack1l1l1l11l_opy_(bstack11l1111_opy_, config, bstack1l_opy_ = {}):
  global bstack11l11ll_opy_
  if not config:
    return
  bstack1111ll_opy_ = bstack111lll1l1_opy_ if not bstack11l11ll_opy_ else ( bstack1ll1l11l_opy_ if bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡱࠩග") in config else bstack111111l1_opy_ )
  data = {
    bstack1l1llll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨඝ"): config[bstack1l1llll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩඞ")],
    bstack1l1llll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫඟ"): config[bstack1l1llll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬච")],
    bstack1l1llll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧඡ"): bstack11l1111_opy_,
    bstack1l1llll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧජ"): {
      bstack1l1llll1l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪඣ"): str(config[bstack1l1llll1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ඤ")]) if bstack1l1llll1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧඥ") in config else bstack1l1llll1l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤඦ"),
      bstack1l1llll1l_opy_ (u"ࠩࡵࡩ࡫࡫ࡲࡳࡧࡵࠫට"): bstack11l1lll_opy_(os.getenv(bstack1l1llll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠧඨ"), bstack1l1llll1l_opy_ (u"ࠦࠧඩ"))),
      bstack1l1llll1l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧඪ"): bstack1l1llll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ණ"),
      bstack1l1llll1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨඬ"): bstack1111ll_opy_,
      bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫත"): config[bstack1l1llll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬථ")]if config[bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ද")] else bstack1l1llll1l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧධ"),
      bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧන"): str(config[bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ඲")]) if bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩඳ") in config else bstack1l1llll1l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤප"),
      bstack1l1llll1l_opy_ (u"ࠩࡲࡷࠬඵ"): sys.platform,
      bstack1l1llll1l_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬබ"): socket.gethostname()
    }
  }
  update(data[bstack1l1llll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧභ")], bstack1l_opy_)
  try:
    response = bstack1l111l1_opy_(bstack1l1llll1l_opy_ (u"ࠬࡖࡏࡔࡖࠪම"), bstack1ll111ll1_opy_, data, config)
    if response:
      logger.debug(bstack1l111lll1_opy_.format(bstack11l1111_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1lll1ll_opy_.format(str(e)))
def bstack1l111l1_opy_(type, url, data, config):
  bstack1111ll1l_opy_ = bstack1llll1l_opy_.format(url)
  proxies = bstack1_opy_(config, bstack1111ll1l_opy_)
  if type == bstack1l1llll1l_opy_ (u"࠭ࡐࡐࡕࡗࠫඹ"):
    response = requests.post(bstack1111ll1l_opy_, json=data,
                    headers={bstack1l1llll1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ය"): bstack1l1llll1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫර")}, auth=(config[bstack1l1llll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ඼")], config[bstack1l1llll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ල")]), proxies=proxies)
  return response
def bstack11l1lll_opy_(framework):
  return bstack1l1llll1l_opy_ (u"ࠦࢀࢃ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣ඾").format(str(framework), __version__) if framework else bstack1l1llll1l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ඿").format(__version__)
def bstack1lll1llll_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack1lllll1_opy_()
    logger.debug(bstack1l11ll11_opy_.format(str(CONFIG)))
    bstack11l1111ll_opy_()
    bstack11lll11l_opy_()
  except Exception as e:
    logger.error(bstack1l1llll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥව") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l11l11_opy_
  atexit.register(bstack1ll1l1ll1_opy_)
  signal.signal(signal.SIGINT, bstack1lll1lll_opy_)
  signal.signal(signal.SIGTERM, bstack1lll1lll_opy_)
def bstack11l11l11_opy_(exctype, value, traceback):
  global bstack1ll1l1ll_opy_
  try:
    for driver in bstack1ll1l1ll_opy_:
      driver.execute_script(
        bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࠮ࠣࠦࡷ࡫ࡡࡴࡱࡱࠦ࠿ࠦࠧශ") + json.dumps(bstack1l1llll1l_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦෂ") + str(value)) + bstack1l1llll1l_opy_ (u"ࠩࢀࢁࠬස"))
  except Exception:
    pass
  bstack1llll11_opy_(value)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1llll11_opy_(message = bstack1l1llll1l_opy_ (u"ࠪࠫහ")):
  global CONFIG
  try:
    if message:
      bstack1l_opy_ = {
        bstack1l1llll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪළ"): str(message)
      }
      bstack1l1l1l11l_opy_(bstack111ll111l_opy_, CONFIG, bstack1l_opy_)
    else:
      bstack1l1l1l11l_opy_(bstack111ll111l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11l11_opy_.format(str(e)))
def bstack1l111111_opy_(bstack1l11111l_opy_, size):
  bstack11l11l11l_opy_ = []
  while len(bstack1l11111l_opy_) > size:
    bstack111lllll1_opy_ = bstack1l11111l_opy_[:size]
    bstack11l11l11l_opy_.append(bstack111lllll1_opy_)
    bstack1l11111l_opy_   = bstack1l11111l_opy_[size:]
  bstack11l11l11l_opy_.append(bstack1l11111l_opy_)
  return bstack11l11l11l_opy_
def bstack1ll11l11_opy_(args):
  if bstack1l1llll1l_opy_ (u"ࠬ࠳࡭ࠨෆ") in args and bstack1l1llll1l_opy_ (u"࠭ࡰࡥࡤࠪ෇") in args:
    return True
  return False
def run_on_browserstack(bstack1llll1ll1_opy_=None, bstack1111l1ll_opy_=None, bstack1l1_opy_=False):
  global CONFIG
  global bstack1ll1lll_opy_
  global bstack111l1l111_opy_
  bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠧࠨ෈")
  if bstack1llll1ll1_opy_ and isinstance(bstack1llll1ll1_opy_, str):
    bstack1llll1ll1_opy_ = eval(bstack1llll1ll1_opy_)
  if bstack1llll1ll1_opy_:
    CONFIG = bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ෉")]
    bstack1ll1lll_opy_ = bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎ්ࠪ")]
    bstack111l1l111_opy_ = bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ෋")]
    bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ෌")
  if not bstack1l1_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack111lll1_opy_)
      return
    if sys.argv[1] == bstack1l1llll1l_opy_ (u"ࠬ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ෍")  or sys.argv[1] == bstack1l1llll1l_opy_ (u"࠭࠭ࡷࠩ෎"):
      logger.info(bstack1l1llll1l_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡐࡺࡶ࡫ࡳࡳࠦࡓࡅࡍࠣࡺࢀࢃࠧා").format(__version__))
      return
    if sys.argv[1] == bstack1l1llll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧැ"):
      bstack11111lll_opy_()
      return
  args = sys.argv
  bstack1lll1llll_opy_()
  global bstack1l11111l1_opy_
  global bstack1ll1llll_opy_
  global bstack1l1ll1111_opy_
  global bstack1l1llll_opy_
  global bstack11l1l111_opy_
  global bstack11l1l1lll_opy_
  global bstack11ll1l11_opy_
  global bstack111ll1l1_opy_
  if not bstack1l11l1l11_opy_:
    if args[1] == bstack1l1llll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩෑ") or args[1] == bstack1l1llll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫි"):
      bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫී")
      args = args[2:]
    elif args[1] == bstack1l1llll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫු"):
      bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ෕")
      args = args[2:]
    elif args[1] == bstack1l1llll1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ූ"):
      bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ෗")
      args = args[2:]
    elif args[1] == bstack1l1llll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪෘ"):
      bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫෙ")
      args = args[2:]
    elif args[1] == bstack1l1llll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫේ"):
      bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬෛ")
      args = args[2:]
    elif args[1] == bstack1l1llll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ො"):
      bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧෝ")
      args = args[2:]
    else:
      if not bstack1l1llll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫෞ") in CONFIG or str(CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬෟ")]).lower() in [bstack1l1llll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ෠"), bstack1l1llll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ෡")]:
        bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ෢")
        args = args[1:]
      elif str(CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ෣")]).lower() == bstack1l1llll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭෤"):
        bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ෥")
        args = args[1:]
      elif str(CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ෦")]).lower() == bstack1l1llll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ෧"):
        bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ෨")
        args = args[1:]
      elif str(CONFIG[bstack1l1llll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ෩")]).lower() == bstack1l1llll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭෪"):
        bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ෫")
        args = args[1:]
      elif str(CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ෬")]).lower() == bstack1l1llll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ෭"):
        bstack1l11l1l11_opy_ = bstack1l1llll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ෮")
        args = args[1:]
      else:
        os.environ[bstack1l1llll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭෯")] = bstack1l11l1l11_opy_
        bstack1111ll1_opy_(bstack1l11lll_opy_)
  global bstack11ll1ll11_opy_
  if bstack1llll1ll1_opy_:
    try:
      os.environ[bstack1l1llll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ෰")] = bstack1l11l1l11_opy_
      bstack1l1l1l11l_opy_(bstack11l1l11l_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack11l11_opy_.format(str(e)))
  global bstack11ll1lll1_opy_
  global bstack111l_opy_
  global bstack1l1l11ll1_opy_
  global bstack1l1lll1l1_opy_
  global bstack11ll1lll_opy_
  global bstack1l11l_opy_
  global bstack1l1l111_opy_
  global bstack11ll1l11l_opy_
  global bstack11lll111l_opy_
  global bstack1ll111l11_opy_
  global bstack1l1ll11l1_opy_
  global bstack1l1l1l_opy_
  global bstack11l1llll1_opy_
  global bstack1l11l1ll_opy_
  global bstack1lllll111_opy_
  global bstack1lll1111_opy_
  global bstack11llll_opy_
  global bstack1l11l111l_opy_
  global bstack11l11ll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1lll1_opy_ = webdriver.Remote.__init__
    bstack111l_opy_ = WebDriver.quit
    bstack1l1ll11l1_opy_ = WebDriver.close
    bstack1l11l1ll_opy_ = WebDriver.get
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11ll1ll11_opy_ = Popen.__init__
  except Exception as e:
    pass
  if bstack111l1lll_opy_():
    if bstack11lll1111_opy_() < version.parse(bstack11l_opy_):
      logger.error(bstack11ll1ll_opy_.format(bstack11lll1111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lllll111_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack1l1l1l1ll_opy_.format(str(e)))
  if bstack1l11l1l11_opy_ != bstack1l1llll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭෱") or (bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧෲ") and not bstack1llll1ll1_opy_):
    bstack1111l11_opy_()
  if (bstack1l11l1l11_opy_ in [bstack1l1llll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧෳ"), bstack1l1llll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ෴"), bstack1l1llll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ෵")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11111_opy_
        bstack11ll1lll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll11l1l1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1lll1l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll11ll1_opy_ + str(e))
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1ll11l1l1_opy_)
    if bstack1l11l1l11_opy_ != bstack1l1llll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ෶"):
      bstack1ll1ll_opy_()
    bstack1l1l11ll1_opy_ = Output.end_test
    bstack1l11l_opy_ = TestStatus.__init__
    bstack11ll1l11l_opy_ = pabot._run
    bstack11lll111l_opy_ = QueueItem.__init__
    bstack1ll111l11_opy_ = pabot._create_command_for_execution
    bstack1l11l111l_opy_ = pabot._report_results
  if bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ෷"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1l11l111_opy_)
    bstack1l1l1l_opy_ = Runner.run_hook
    bstack11l1llll1_opy_ = Step.run
  if bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭෸"):
    try:
      from _pytest.config import Config
      bstack1lll1111_opy_ = Config.getoption
      from _pytest import runner
      bstack11llll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11111111_opy_)
    try:
      from pytest_bdd import reporting
      bstack11l11ll1l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1l1llll1l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ෹"))
  if bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ෺"):
    bstack1ll1llll_opy_ = True
    if bstack1llll1ll1_opy_ and bstack1l1_opy_:
      bstack11l1l111_opy_ = CONFIG.get(bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭෻"), {}).get(bstack1l1llll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ෼"))
      bstack1ll1ll1l_opy_(bstack11l1ll111_opy_)
    elif bstack1llll1ll1_opy_:
      bstack11l1l111_opy_ = CONFIG.get(bstack1l1llll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ෽"), {}).get(bstack1l1llll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ෾"))
      global bstack1ll1l1ll_opy_
      try:
        if bstack1ll11l11_opy_(bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ෿")]) and multiprocessing.current_process().name == bstack1l1llll1l_opy_ (u"ࠧ࠱ࠩ฀"):
          bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫก")].remove(bstack1l1llll1l_opy_ (u"ࠩ࠰ࡱࠬข"))
          bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ฃ")].remove(bstack1l1llll1l_opy_ (u"ࠫࡵࡪࡢࠨค"))
          bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨฅ")] = bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩฆ")][0]
          with open(bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪง")], bstack1l1llll1l_opy_ (u"ࠨࡴࠪจ")) as f:
            bstack1l1llll1_opy_ = f.read()
          bstack1l1111111_opy_ = bstack1l1llll1l_opy_ (u"ࠤࠥࠦ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡧ࡯ࠥ࡯࡭ࡱࡱࡵࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥ࠼ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩ࠭ࢁࡽࠪ࠽ࠣࡪࡷࡵ࡭ࠡࡲࡧࡦࠥ࡯࡭ࡱࡱࡵࡸࠥࡖࡤࡣ࠽ࠣࡳ࡬ࡥࡤࡣࠢࡀࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭࠾ࠎࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࡺࡲࡺ࠼ࠍࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࡪࡾࡣࡦࡲࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡢࡵࠣࡩ࠿ࠐࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࡳ࡬ࡥࡤࡣࠪࡶࡩࡱ࡬ࠬࡢࡴࡪ࠰ࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠩࠋࡒࡧࡦ࠳ࡪ࡯ࡠࡤࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࡖࡤࡣࠪࠬ࠲ࡸ࡫ࡴࡠࡶࡵࡥࡨ࡫ࠨࠪ࡞ࡱࠦࠧࠨฉ").format(str(bstack1llll1ll1_opy_))
          bstack1ll1ll1ll_opy_ = bstack1l1111111_opy_ + bstack1l1llll1_opy_
          bstack11l11lll1_opy_ = bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ช")] + bstack1l1llll1l_opy_ (u"ࠫࡤࡨࡳࡵࡣࡦ࡯ࡤࡺࡥ࡮ࡲ࠱ࡴࡾ࠭ซ")
          with open(bstack11l11lll1_opy_, bstack1l1llll1l_opy_ (u"ࠬࡽࠧฌ")):
            pass
          with open(bstack11l11lll1_opy_, bstack1l1llll1l_opy_ (u"ࠨࡷࠬࠤญ")) as f:
            f.write(bstack1ll1ll1ll_opy_)
          import subprocess
          bstack11lll1l11_opy_ = subprocess.run([bstack1l1llll1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢฎ"), bstack11l11lll1_opy_])
          if os.path.exists(bstack11l11lll1_opy_):
            os.unlink(bstack11l11lll1_opy_)
          os._exit(bstack11lll1l11_opy_.returncode)
        else:
          if bstack1ll11l11_opy_(bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫฏ")]):
            bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬฐ")].remove(bstack1l1llll1l_opy_ (u"ࠪ࠱ࡲ࠭ฑ"))
            bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧฒ")].remove(bstack1l1llll1l_opy_ (u"ࠬࡶࡤࡣࠩณ"))
            bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩด")] = bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪต")][0]
          bstack1ll1ll1l_opy_(bstack11l1ll111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫถ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l1llll1l_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫท")] = bstack1l1llll1l_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬธ")
          mod_globals[bstack1l1llll1l_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭น")] = os.path.abspath(bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨบ")])
          exec(open(bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩป")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l1llll1l_opy_ (u"ࠧࡄࡣࡸ࡫࡭ࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠧผ").format(str(e)))
          for driver in bstack1ll1l1ll_opy_:
            bstack1111l1ll_opy_.append({
              bstack1l1llll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ฝ"): bstack1llll1ll1_opy_[bstack1l1llll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬพ")],
              bstack1l1llll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩฟ"): str(e),
              bstack1l1llll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪภ"): multiprocessing.current_process().name
            })
            driver.execute_script(
              bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡸࡺࡡࡵࡷࡶࠦ࠿ࠨࡦࡢ࡫࡯ࡩࡩࠨࠬࠡࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠤࠬม") + json.dumps(bstack1l1llll1l_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤย") + str(e)) + bstack1l1llll1l_opy_ (u"ࠧࡾࡿࠪร"))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1ll1l1ll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      bstack11ll11l1l_opy_()
      bstack11111ll_opy_()
      bstack1l11111ll_opy_ = {
        bstack1l1llll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫฤ"): args[0],
        bstack1l1llll1l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩล"): CONFIG,
        bstack1l1llll1l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫฦ"): bstack1ll1lll_opy_,
        bstack1l1llll1l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ว"): bstack111l1l111_opy_
      }
      if bstack1l1llll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨศ") in CONFIG:
        bstack1lll1ll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1llll1l1_opy_ = manager.list()
        if bstack1ll11l11_opy_(args):
          for index, platform in enumerate(CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩษ")]):
            if index == 0:
              bstack1l11111ll_opy_[bstack1l1llll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪส")] = args
            bstack1lll1ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                          target=run_on_browserstack, args=(bstack1l11111ll_opy_, bstack1llll1l1_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫห")]):
            bstack1lll1ll1l_opy_.append(multiprocessing.Process(name=str(index),
                                          target=run_on_browserstack, args=(bstack1l11111ll_opy_, bstack1llll1l1_opy_)))
        for t in bstack1lll1ll1l_opy_:
          t.start()
        for t in bstack1lll1ll1l_opy_:
          t.join()
        bstack11ll1l11_opy_ = list(bstack1llll1l1_opy_)
      else:
        if bstack1ll11l11_opy_(args):
          bstack1l11111ll_opy_[bstack1l1llll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬฬ")] = args
          test = multiprocessing.Process(name=str(0),
                                        target=run_on_browserstack, args=(bstack1l11111ll_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll1ll1l_opy_(bstack11l1ll111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l1llll1l_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬอ")] = bstack1l1llll1l_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ฮ")
          mod_globals[bstack1l1llll1l_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧฯ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬะ") or bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ั"):
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1ll11l1l1_opy_)
    bstack11ll11l1l_opy_()
    bstack1ll1ll1l_opy_(bstack11l11l111_opy_)
    if bstack1l1llll1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭า") in args:
      i = args.index(bstack1l1llll1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧำ"))
      args.pop(i)
      args.pop(i)
    args.insert(0, str(bstack1l11111l1_opy_))
    args.insert(0, str(bstack1l1llll1l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨิ")))
    pabot.main(args)
  elif bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬี"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1ll11l1l1_opy_)
    for a in args:
      if bstack1l1llll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫึ") in a:
        bstack1l1llll_opy_ = int(a.split(bstack1l1llll1l_opy_ (u"࠭࠺ࠨื"))[1])
      if bstack1l1llll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕุࠫ") in a:
        bstack11l1l111_opy_ = str(a.split(bstack1l1llll1l_opy_ (u"ࠨ࠼ูࠪ"))[1])
      if bstack1l1llll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔฺࠩ") in a:
        bstack11l1l1lll_opy_ = str(a.split(bstack1l1llll1l_opy_ (u"ࠪ࠾ࠬ฻"))[1])
    bstack1lll11lll_opy_ = None
    if bstack1l1llll1l_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪ฼") in args:
      i = args.index(bstack1l1llll1l_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ฽"))
      args.pop(i)
      bstack1lll11lll_opy_ = args.pop(i)
    if bstack1lll11lll_opy_ is not None:
      global bstack11l11l1l1_opy_
      bstack11l11l1l1_opy_ = bstack1lll11lll_opy_
    bstack1ll1ll1l_opy_(bstack11l11l111_opy_)
    run_cli(args)
  elif bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭฾"):
    try:
      from _pytest.config import _prepareconfig
      from _pytest.config import Config
      from _pytest import runner
      import importlib
      bstack1lllllll1_opy_ = importlib.find_loader(bstack1l1llll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ฿"))
    except Exception as e:
      logger.warn(e, bstack11111111_opy_)
    bstack11ll11l1l_opy_()
    try:
      if bstack1l1llll1l_opy_ (u"ࠨ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠪเ") in args:
        i = args.index(bstack1l1llll1l_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫแ"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l1llll1l_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭โ") in args:
        i = args.index(bstack1l1llll1l_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧใ"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l1llll1l_opy_ (u"ࠬ࠳ࡰࠨไ") in args:
        i = args.index(bstack1l1llll1l_opy_ (u"࠭࠭ࡱࠩๅ"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l1llll1l_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨๆ") in args:
        i = args.index(bstack1l1llll1l_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ็"))
        args.pop(i+1)
        args.pop(i)
      if bstack1l1llll1l_opy_ (u"ࠩ࠰ࡲ่ࠬ") in args:
        i = args.index(bstack1l1llll1l_opy_ (u"ࠪ࠱ࡳ้࠭"))
        args.pop(i+1)
        args.pop(i)
    except Exception as exc:
      logger.error(str(exc))
    config = _prepareconfig(args)
    bstack111ll111_opy_ = config.args
    bstack11l1ll11_opy_ = config.invocation_params.args
    bstack11l1ll11_opy_ = list(bstack11l1ll11_opy_)
    bstack1ll1l1111_opy_ = [os.path.normpath(item) for item in bstack111ll111_opy_]
    bstack11lllll1_opy_ = [os.path.normpath(item) for item in bstack11l1ll11_opy_]
    bstack1l111l111_opy_ = [item for item in bstack11lllll1_opy_ if item not in bstack1ll1l1111_opy_]
    if bstack1l1llll1l_opy_ (u"ࠫ࠲࠳ࡣࡢࡥ࡫ࡩ࠲ࡩ࡬ࡦࡣࡵ๊ࠫ") not in bstack1l111l111_opy_:
      bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠬ࠳࠭ࡤࡣࡦ࡬ࡪ࠳ࡣ࡭ࡧࡤࡶ๋ࠬ"))
    import platform as pf
    if pf.system().lower() == bstack1l1llll1l_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧ์"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111ll111_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11lll1ll_opy_)))
                    for bstack11lll1ll_opy_ in bstack111ll111_opy_]
    if (bstack1ll111l1l_opy_):
      bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠧ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫํ"))
      bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠨࡖࡵࡹࡪ࠭๎"))
    try:
      from pytest_bdd import reporting
      bstack111ll1l1_opy_ = True
    except Exception as e:
      pass
    if (not bstack111ll1l1_opy_):
      bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠩ࠰ࡴࠬ๏"))
      bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡲ࡯ࡹ࡬࡯࡮ࠨ๐"))
    bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠫ࠲࠳ࡤࡳ࡫ࡹࡩࡷ࠭๑"))
    bstack1l111l111_opy_.append(bstack1l1llll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ๒"))
    bstack1l111l1ll_opy_ = []
    for spec in bstack111ll111_opy_:
      bstack1111l11l_opy_ = []
      bstack1111l11l_opy_.append(spec)
      bstack1111l11l_opy_ += bstack1l111l111_opy_
      bstack1l111l1ll_opy_.append(bstack1111l11l_opy_)
    bstack1l1ll1111_opy_ = True
    bstack1llll1111_opy_ = 1
    if bstack1l1llll1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭๓") in CONFIG:
      bstack1llll1111_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ๔")]
    bstack111l11l11_opy_ = int(bstack1llll1111_opy_)*int(len(CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ๕")]))
    execution_items = []
    for bstack1111l11l_opy_ in bstack1l111l1ll_opy_:
      for index, _ in enumerate(CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ๖")]):
        item = {}
        item[bstack1l1llll1l_opy_ (u"ࠪࡥࡷ࡭ࠧ๗")] = bstack1111l11l_opy_
        item[bstack1l1llll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ๘")] = index
        execution_items.append(item)
    bstack11l1ll_opy_ = bstack1l111111_opy_(execution_items, bstack111l11l11_opy_)
    for execution_item in bstack11l1ll_opy_:
      bstack1lll1ll1l_opy_ = []
      for item in execution_item:
        bstack1lll1ll1l_opy_.append(bstack1l11ll_opy_(name=str(item[bstack1l1llll1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ๙")]),
                                            target=bstack111l1l1ll_opy_,
                                            args=(item[bstack1l1llll1l_opy_ (u"࠭ࡡࡳࡩࠪ๚")],)))
      for t in bstack1lll1ll1l_opy_:
        t.start()
      for t in bstack1lll1ll1l_opy_:
        t.join()
  elif bstack1l11l1l11_opy_ == bstack1l1llll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ๛"):
    try:
      from behave.__main__ import main as bstack11l111lll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll1l1l_opy_(e, bstack1l11l111_opy_)
    bstack11ll11l1l_opy_()
    bstack1l1ll1111_opy_ = True
    bstack1llll1111_opy_ = 1
    if bstack1l1llll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ๜") in CONFIG:
      bstack1llll1111_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ๝")]
    bstack111l11l11_opy_ = int(bstack1llll1111_opy_)*int(len(CONFIG[bstack1l1llll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭๞")]))
    config = Configuration(args)
    bstack111l1ll1l_opy_ = config.paths
    if len(bstack111l1ll1l_opy_) == 0:
      import glob
      pattern = bstack1l1llll1l_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪ๟")
      bstack11l1ll1l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11l1ll1l_opy_)
      config = Configuration(args)
      bstack111l1ll1l_opy_ = config.paths
    bstack111ll111_opy_ = [os.path.normpath(item) for item in bstack111l1ll1l_opy_]
    bstack1111lll1_opy_ = [os.path.normpath(item) for item in args]
    bstack1l11lll11_opy_ = [item for item in bstack1111lll1_opy_ if item not in bstack111ll111_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l1llll1l_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭๠"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111ll111_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11lll1ll_opy_)))
                    for bstack11lll1ll_opy_ in bstack111ll111_opy_]
    bstack1l111l1ll_opy_ = []
    for spec in bstack111ll111_opy_:
      bstack1111l11l_opy_ = []
      bstack1111l11l_opy_ += bstack1l11lll11_opy_
      bstack1111l11l_opy_.append(spec)
      bstack1l111l1ll_opy_.append(bstack1111l11l_opy_)
    execution_items = []
    for bstack1111l11l_opy_ in bstack1l111l1ll_opy_:
      for index, _ in enumerate(CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ๡")]):
        item = {}
        item[bstack1l1llll1l_opy_ (u"ࠧࡢࡴࡪࠫ๢")] = bstack1l1llll1l_opy_ (u"ࠨࠢࠪ๣").join(bstack1111l11l_opy_)
        item[bstack1l1llll1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ๤")] = index
        execution_items.append(item)
    bstack11l1ll_opy_ = bstack1l111111_opy_(execution_items, bstack111l11l11_opy_)
    for execution_item in bstack11l1ll_opy_:
      bstack1lll1ll1l_opy_ = []
      for item in execution_item:
        bstack1lll1ll1l_opy_.append(bstack1l11ll_opy_(name=str(item[bstack1l1llll1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ๥")]),
                                            target=bstack11ll111l_opy_,
                                            args=(item[bstack1l1llll1l_opy_ (u"ࠫࡦࡸࡧࠨ๦")],)))
      for t in bstack1lll1ll1l_opy_:
        t.start()
      for t in bstack1lll1ll1l_opy_:
        t.join()
  else:
    bstack1111ll1_opy_(bstack1l11lll_opy_)
  if not bstack1llll1ll1_opy_:
    bstack1ll111ll_opy_()
def browserstack_initialize(bstack111lllll_opy_=None):
  run_on_browserstack(bstack111lllll_opy_, None, True)
def bstack1ll111ll_opy_():
  [bstack11lllll11_opy_, bstack1l1l1ll_opy_] = bstack111l111_opy_()
  if bstack11lllll11_opy_ is not None and bstack1l1l1l1l_opy_() != -1:
    sessions = bstack111ll1l1l_opy_(bstack11lllll11_opy_)
    bstack111l11l1l_opy_(sessions, bstack1l1l1ll_opy_)
def bstack1l111lll_opy_(bstack1l11ll1_opy_):
    if bstack1l11ll1_opy_:
        return bstack1l11ll1_opy_.capitalize()
    else:
        return bstack1l11ll1_opy_
def bstack1l1l1111_opy_(bstack1llllll1l_opy_):
    if bstack1l1llll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ๧") in bstack1llllll1l_opy_ and bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ๨")] != bstack1l1llll1l_opy_ (u"ࠧࠨ๩"):
        return bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭๪")]
    else:
        bstack111l111ll_opy_ = bstack1l1llll1l_opy_ (u"ࠤࠥ๫")
        if bstack1l1llll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ๬") in bstack1llllll1l_opy_ and bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ๭")] != None:
            bstack111l111ll_opy_ += bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ๮")] + bstack1l1llll1l_opy_ (u"ࠨࠬࠡࠤ๯")
            if bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠧࡰࡵࠪ๰")] == bstack1l1llll1l_opy_ (u"ࠣ࡫ࡲࡷࠧ๱"):
                bstack111l111ll_opy_ += bstack1l1llll1l_opy_ (u"ࠤ࡬ࡓࡘࠦࠢ๲")
            bstack111l111ll_opy_ += (bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ๳")] or bstack1l1llll1l_opy_ (u"ࠫࠬ๴"))
            return bstack111l111ll_opy_
        else:
            bstack111l111ll_opy_ += bstack1l111lll_opy_(bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭๵")]) + bstack1l1llll1l_opy_ (u"ࠨࠠࠣ๶") + (bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ๷")] or bstack1l1llll1l_opy_ (u"ࠨࠩ๸")) + bstack1l1llll1l_opy_ (u"ࠤ࠯ࠤࠧ๹")
            if bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"ࠪࡳࡸ࠭๺")] == bstack1l1llll1l_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧ๻"):
                bstack111l111ll_opy_ += bstack1l1llll1l_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥ๼")
            bstack111l111ll_opy_ += bstack1llllll1l_opy_[bstack1l1llll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ๽")] or bstack1l1llll1l_opy_ (u"ࠧࠨ๾")
            return bstack111l111ll_opy_
def bstack11llllll_opy_(bstack11llll111_opy_):
    if bstack11llll111_opy_ == bstack1l1llll1l_opy_ (u"ࠣࡦࡲࡲࡪࠨ๿"):
        return bstack1l1llll1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ຀")
    elif bstack11llll111_opy_ == bstack1l1llll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥກ"):
        return bstack1l1llll1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧຂ")
    elif bstack11llll111_opy_ == bstack1l1llll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ຃"):
        return bstack1l1llll1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ຄ")
    elif bstack11llll111_opy_ == bstack1l1llll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ຅"):
        return bstack1l1llll1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪຆ")
    elif bstack11llll111_opy_ == bstack1l1llll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥງ"):
        return bstack1l1llll1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨຈ")
    elif bstack11llll111_opy_ == bstack1l1llll1l_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧຉ"):
        return bstack1l1llll1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ຊ")
    else:
        return bstack1l1llll1l_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪ຋")+bstack1l111lll_opy_(bstack11llll111_opy_)+bstack1l1llll1l_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ຌ")
def bstack1111l1_opy_(session):
    return bstack1l1llll1l_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨຍ").format(session[bstack1l1llll1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ຎ")],bstack1l1l1111_opy_(session), bstack11llllll_opy_(session[bstack1l1llll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩຏ")]), bstack11llllll_opy_(session[bstack1l1llll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫຐ")]), bstack1l111lll_opy_(session[bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ຑ")] or session[bstack1l1llll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ຒ")] or bstack1l1llll1l_opy_ (u"ࠧࠨຓ")) + bstack1l1llll1l_opy_ (u"ࠣࠢࠥດ") + (session[bstack1l1llll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫຕ")] or bstack1l1llll1l_opy_ (u"ࠪࠫຖ")), session[bstack1l1llll1l_opy_ (u"ࠫࡴࡹࠧທ")] + bstack1l1llll1l_opy_ (u"ࠧࠦࠢຘ") + session[bstack1l1llll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪນ")], session[bstack1l1llll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩບ")] or bstack1l1llll1l_opy_ (u"ࠨࠩປ"), session[bstack1l1llll1l_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ຜ")] if session[bstack1l1llll1l_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧຝ")] else bstack1l1llll1l_opy_ (u"ࠫࠬພ"))
def bstack111l11l1l_opy_(sessions, bstack1l1l1ll_opy_):
  try:
    bstack1ll11lll_opy_ = bstack1l1llll1l_opy_ (u"ࠧࠨຟ")
    if not os.path.exists(bstack11l1ll1ll_opy_):
      os.mkdir(bstack11l1ll1ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1llll1l_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫຠ")), bstack1l1llll1l_opy_ (u"ࠧࡳࠩມ")) as f:
      bstack1ll11lll_opy_ = f.read()
    bstack1ll11lll_opy_ = bstack1ll11lll_opy_.replace(bstack1l1llll1l_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬຢ"), str(len(sessions)))
    bstack1ll11lll_opy_ = bstack1ll11lll_opy_.replace(bstack1l1llll1l_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩຣ"), bstack1l1l1ll_opy_)
    bstack1ll11lll_opy_ = bstack1ll11lll_opy_.replace(bstack1l1llll1l_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫ຤"), sessions[0].get(bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨລ")) if sessions[0] else bstack1l1llll1l_opy_ (u"ࠬ࠭຦"))
    with open(os.path.join(bstack11l1ll1ll_opy_, bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪວ")), bstack1l1llll1l_opy_ (u"ࠧࡸࠩຨ")) as stream:
      stream.write(bstack1ll11lll_opy_.split(bstack1l1llll1l_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬຩ"))[0])
      for session in sessions:
        stream.write(bstack1111l1_opy_(session))
      stream.write(bstack1ll11lll_opy_.split(bstack1l1llll1l_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ສ"))[1])
    logger.info(bstack1l1llll1l_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭ຫ").format(bstack11l1ll1ll_opy_));
  except Exception as e:
    logger.debug(bstack1l111ll1_opy_.format(str(e)))
def bstack111ll1l1l_opy_(bstack11lllll11_opy_):
  global CONFIG
  try:
    host = bstack1l1llll1l_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧຬ") if bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡱࠩອ") in CONFIG else bstack1l1llll1l_opy_ (u"࠭ࡡࡱ࡫ࠪຮ")
    user = CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩຯ")]
    key = CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫະ")]
    bstack11l1l1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨັ") if bstack1l1llll1l_opy_ (u"ࠪࡥࡵࡶࠧາ") in CONFIG else bstack1l1llll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ຳ")
    url = bstack1l1llll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪິ").format(user, key, host, bstack11l1l1ll_opy_, bstack11lllll11_opy_)
    headers = {
      bstack1l1llll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬີ"): bstack1l1llll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪຶ"),
    }
    proxies = bstack1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack1l1llll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ື")], response.json()))
  except Exception as e:
    logger.debug(bstack11l1l_opy_.format(str(e)))
def bstack111l111_opy_():
  global CONFIG
  try:
    if bstack1l1llll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩຸࠬ") in CONFIG:
      host = bstack1l1llll1l_opy_ (u"ࠪࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩູ࠭") if bstack1l1llll1l_opy_ (u"ࠫࡦࡶࡰࠨ຺") in CONFIG else bstack1l1llll1l_opy_ (u"ࠬࡧࡰࡪࠩົ")
      user = CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨຼ")]
      key = CONFIG[bstack1l1llll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪຽ")]
      bstack11l1l1ll_opy_ = bstack1l1llll1l_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ຾") if bstack1l1llll1l_opy_ (u"ࠩࡤࡴࡵ࠭຿") in CONFIG else bstack1l1llll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬເ")
      url = bstack1l1llll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࢀࢃ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠴ࡪࡴࡱࡱࠫແ").format(user, key, host, bstack11l1l1ll_opy_)
      headers = {
        bstack1l1llll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫໂ"): bstack1l1llll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩໃ"),
      }
      if bstack1l1llll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩໄ") in CONFIG:
        params = {bstack1l1llll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭໅"):CONFIG[bstack1l1llll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬໆ")], bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭໇"):CONFIG[bstack1l1llll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ່࠭")]}
      else:
        params = {bstack1l1llll1l_opy_ (u"ࠬࡴࡡ࡮ࡧ້ࠪ"):CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦ໊ࠩ")]}
      proxies = bstack1_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack11l1l1l1_opy_ = response.json()[0][bstack1l1llll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡧࡻࡩ࡭ࡦ໋ࠪ")]
        if bstack11l1l1l1_opy_:
          bstack1l1l1ll_opy_ = bstack11l1l1l1_opy_[bstack1l1llll1l_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬ໌")].split(bstack1l1llll1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤ࠯ࡥࡹ࡮ࡲࡤࠨໍ"))[0] + bstack1l1llll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵ࠲ࠫ໎") + bstack11l1l1l1_opy_[bstack1l1llll1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ໏")]
          logger.info(bstack111l1l11_opy_.format(bstack1l1l1ll_opy_))
          bstack1l11111_opy_ = CONFIG[bstack1l1llll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ໐")]
          if bstack1l1llll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໑") in CONFIG:
            bstack1l11111_opy_ += bstack1l1llll1l_opy_ (u"ࠧࠡࠩ໒") + CONFIG[bstack1l1llll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໓")]
          if bstack1l11111_opy_!= bstack11l1l1l1_opy_[bstack1l1llll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ໔")]:
            logger.debug(bstack1ll11l1ll_opy_.format(bstack11l1l1l1_opy_[bstack1l1llll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ໕")], bstack1l11111_opy_))
          return [bstack11l1l1l1_opy_[bstack1l1llll1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ໖")], bstack1l1l1ll_opy_]
    else:
      logger.warn(bstack1111111l_opy_)
  except Exception as e:
    logger.debug(bstack11l1ll1_opy_.format(str(e)))
  return [None, None]
def bstack11ll1ll1_opy_(url, bstack11111ll1_opy_=False):
  global CONFIG
  global bstack11ll1l1ll_opy_
  if not bstack11ll1l1ll_opy_:
    hostname = bstack1l1l1l1_opy_(url)
    is_private = bstack111lll111_opy_(hostname)
    if (bstack1l1llll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ໗") in CONFIG and not CONFIG[bstack1l1llll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ໘")]) and (is_private or bstack11111ll1_opy_):
      bstack11ll1l1ll_opy_ = hostname
def bstack1l1l1l1_opy_(url):
  return urlparse(url).hostname
def bstack111lll111_opy_(hostname):
  for bstack1l11lll1l_opy_ in bstack1l1111_opy_:
    regex = re.compile(bstack1l11lll1l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l11ll11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
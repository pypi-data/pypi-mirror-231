# coding: UTF-8
import sys
bstack1llll_opy_ = sys.version_info [0] == 2
bstack111l_opy_ = 2048
bstack1_opy_ = 7
def bstackl_opy_ (bstack11ll_opy_):
    global bstack111_opy_
    bstack1ll1_opy_ = ord (bstack11ll_opy_ [-1])
    bstack1111_opy_ = bstack11ll_opy_ [:-1]
    bstack1ll1l_opy_ = bstack1ll1_opy_ % len (bstack1111_opy_)
    bstack1l_opy_ = bstack1111_opy_ [:bstack1ll1l_opy_] + bstack1111_opy_ [bstack1ll1l_opy_:]
    if bstack1llll_opy_:
        bstack11_opy_ = unicode () .join ([unichr (ord (char) - bstack111l_opy_ - (bstack1lll1_opy_ + bstack1ll1_opy_) % bstack1_opy_) for bstack1lll1_opy_, char in enumerate (bstack1l_opy_)])
    else:
        bstack11_opy_ = str () .join ([chr (ord (char) - bstack111l_opy_ - (bstack1lll1_opy_ + bstack1ll1_opy_) % bstack1_opy_) for bstack1lll1_opy_, char in enumerate (bstack1l_opy_)])
    return eval (bstack11_opy_)
import threading
import pytest
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
def bstack1l1_opy_(page, bstack1l1l_opy_):
  try:
    page.evaluate(bstackl_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧࠀ"), bstackl_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩࠁ")+ json.dumps(bstack1l1l_opy_) + bstackl_opy_ (u"ࠨࡽࡾࠤࠂ"))
  except Exception as e:
    print(bstackl_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧࠃ"), e)
def bstack11l_opy_(page, message, level):
  try:
    page.evaluate(bstackl_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤࠄ"), bstackl_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧࠅ") + json.dumps(message) + bstackl_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭ࠆ") + json.dumps(level) + bstackl_opy_ (u"ࠫࢂࢃࠧࠇ"))
  except Exception as e:
    print(bstackl_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽࠣࠈ"), e)
def bstack1ll11_opy_(page, status, message = bstackl_opy_ (u"ࠨࠢࠉ")):
  try:
    if(status == bstackl_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢࠊ")):
      page.evaluate(bstackl_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤࠋ"), bstackl_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡴࡨࡥࡸࡵ࡮ࠣ࠼ࠪࠌ") + json.dumps(bstackl_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࠧࠍ") + str(message)) + bstackl_opy_ (u"ࠫ࠱ࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠨࠎ") + json.dumps(status) + bstackl_opy_ (u"ࠧࢃࡽࠣࠏ"))
    else:
      page.evaluate(bstackl_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢࠐ"), bstackl_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡳࡵࡣࡷࡹࡸࠨ࠺ࠨࠑ") + json.dumps(status) + bstackl_opy_ (u"ࠣࡿࢀࠦࠒ"))
  except Exception as e:
    print(bstackl_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡿࢂࠨࠓ"), e)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1l11_opy_ = item.config.getoption(bstackl_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬࠔ"))
    plugins = item.config.getoption(bstackl_opy_ (u"ࠦࡵࡲࡵࡨ࡫ࡱࡷࠧࠕ"))
    if(bstackl_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠥࠖ") not in plugins):
        return
    report = outcome.get_result()
    summary = []
    driver = getattr(item, bstackl_opy_ (u"ࠨ࡟ࡥࡴ࡬ࡺࡪࡸࠢࠗ"), None)
    page = getattr(item, bstackl_opy_ (u"ࠢࡠࡲࡤ࡫ࡪࠨ࠘"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if(driver is not None):
        bstack1ll_opy_(item, report, summary, bstack1l11_opy_)
    if(page is not None):
        bstack1lll_opy_(item, report, summary, bstack1l11_opy_)
def bstack1ll_opy_(item, report, summary, bstack1l11_opy_):
    if report.when in [bstackl_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ࠙"), bstackl_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦࠚ")]:
            return
    if(str(bstack1l11_opy_).lower() != bstackl_opy_ (u"ࠪࡸࡷࡻࡥࠨࠛ")):
        item._driver.execute_script(bstackl_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩࠜ") + json.dumps(report.nodeid) + bstackl_opy_ (u"ࠬࢃࡽࠨࠝ"))
    passed = report.passed or (report.failed and hasattr(report, bstackl_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣࠞ")))
    bstack11l1_opy_ = bstackl_opy_ (u"ࠢࠣࠟ")
    if not passed:
        try:
            bstack11l1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstackl_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣࠠ").format(e)
            )
    if (bstack11l1_opy_ != bstackl_opy_ (u"ࠤࠥࠡ")):
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11l1_opy_))
    try:
        if (passed):
            item._driver.execute_script(
                    bstackl_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬࠢ")
                    + json.dumps(bstackl_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧࠣ"))
                    + bstackl_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢࠤ")
                )
        else:
            item._driver.execute_script(
                    bstackl_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩࠥ")
                    + json.dumps(str(bstack11l1_opy_))
                    + bstackl_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠤࠦ")
                )
    except Exception as e:
        summary.append(bstackl_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨࠧ").format(e))
def bstack1lll_opy_(item, report, summary, bstack1l11_opy_):
    if report.when in [bstackl_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣࠨ"), bstackl_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧࠩ")]:
            return
    if(str(bstack1l11_opy_).lower() != bstackl_opy_ (u"ࠫࡹࡸࡵࡦࠩࠪ")):
        bstack1l1_opy_(item._page, report.nodeid)
    passed = report.passed or (report.failed and hasattr(report, bstackl_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢࠫ")))
    bstack11l1_opy_ = bstackl_opy_ (u"ࠨࠢࠬ")
    if not passed:
        try:
            bstack11l1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstackl_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢ࠭").format(e)
            )
    try:
        if passed:
            bstack1ll11_opy_(item._page, bstackl_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ࠮"))
        else:
            if bstack11l1_opy_:
                bstack11l_opy_(item._page, str(bstack11l1_opy_), bstackl_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ࠯"))
                bstack1ll11_opy_(item._page, bstackl_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ࠰"), str(bstack11l1_opy_))
            else:
                bstack1ll11_opy_(item._page, bstackl_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࠱"))
    except Exception as e:
        summary.append(bstackl_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁ࠰ࡾࠤ࠲").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstackl_opy_ (u"ࠨ࠭࠮ࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠳"), default=bstackl_opy_ (u"ࠢࡇࡣ࡯ࡷࡪࠨ࠴"), help=bstackl_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡦࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠢ࠵"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstackl_opy_ (u"ࠤ࠰࠱ࡩࡸࡩࡷࡧࡵࠦ࠶"), action=bstackl_opy_ (u"ࠥࡷࡹࡵࡲࡦࠤ࠷"), default=bstackl_opy_ (u"ࠦࡨ࡮ࡲࡰ࡯ࡨࠦ࠸"),
                        help=bstackl_opy_ (u"ࠧࡊࡲࡪࡸࡨࡶࠥࡺ࡯ࠡࡴࡸࡲࠥࡺࡥࡴࡶࡶࠦ࠹"))
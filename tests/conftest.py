import pytest
import allure

@pytest.fixture()
def set_up_tear_down(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.saucedemo.com")
    
    # Start tracing
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield page
    
    # Stop tracing and save the trace
    trace_path = "trace.zip"
    page.context.tracing.stop(path=trace_path)
    
    # Attach trace to Allure report
    allure.attach.file(trace_path, name="Trace", attachment_type=allure.attachment_type.ZIP)

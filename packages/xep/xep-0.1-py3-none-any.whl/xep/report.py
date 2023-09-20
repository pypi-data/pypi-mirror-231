import io
import logging
import time

from openpyxl import load_workbook

from xep.worksheet import WorksheetTemplate

logger = logging.getLogger(__name__)


def make_report(report_template, report_data):
    begin_timestamp = time.time()

    wb = load_workbook(report_template)

    worksheet_templates = [
        (ws, WorksheetTemplate(wb, ws)) for ws in wb.worksheets
    ]

    for ws, wst in worksheet_templates:
        logger.debug(f"Processing worksheet \"{ws.title}\"")

        if wst.context:
            if wst.context in report_data:
                page_data = report_data[wst.context]
            else:
                raise KeyError(f"Cannot find context with name \"{wst.context}\" for page \"{ws.title}\"")

            if wst.multiply:
                origin_ws = ws
                for single_page_data in page_data:
                    ws = wb.copy_worksheet(origin_ws)
                    wb.move_sheet(ws, wb.index(origin_ws) - wb.index(ws))
                    wst.apply(ws, single_page_data)
                wb.remove(origin_ws)
            else:
                wst.apply(
                    ws,
                    page_data
                )

    logger.debug("Writing report")
    # wb.save('/home/p.ilyin/Documents/test_result.xlsx')

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    time_left = time.time() - begin_timestamp
    logger.debug(f"Report created in {time_left}")

    return buffer

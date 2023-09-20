import typer
from ariksa_policy_cli.app.modules.utils.send_request import SendRequest
from ariksa_policy_cli.app.schemas.resource import HTTPMethods, APIResources, WorkflowStatus, WorkflowType
import asyncio
from loguru import logger
import time

app = typer.Typer()


async def _is_snapshot_complete(snapshot_id: str, shared_secret, account_id: str) -> bool:
    logger.info("Waiting for processing to complete")
    s_req = SendRequest(shared_secret=shared_secret)
    is_complete = False
    while not is_complete:
        latest_workflow = await s_req.send_request(
            method=HTTPMethods.GET,
            resource=APIResources.WORKFLOWS.value,
            response_model=dict,
            workflow_type=WorkflowType.snapshot_processing.value,
            account_id=account_id,
            size=2,
        )
        if latest_workflow.get('items'):
            latest_snapshot = latest_workflow.get('items')[1].get('identifier')
            status = latest_workflow.get('items')[1].get('status')
            if status == WorkflowStatus.success.value and latest_snapshot == snapshot_id:
                logger.info("Snapshot Successfull")
                return latest_snapshot
        logger.info("Snapshot Processing not completing. Waiting for for 10s")
        time.sleep(10)
        pass

async def print_report(account_id, shared_secret):
    blueprint_id = '38091076-b4b8-4ee3-aaed-aa647eef9d60'
    s_req = SendRequest(shared_secret=shared_secret)
    report = await s_req.send_request(
        method=HTTPMethods.GET,
        resource=APIResources.REPORT.value,
        response_model=dict,
        account_id=account_id,
        blueprint_id=blueprint_id,
    )
    for each in report.get('items'):
        logger.info(each)

@app.command()
def trigger_discovery(branch: str, account_id:str, shared_secret: str):
    s_req = SendRequest(shared_secret=shared_secret)
    # Trigger gitlab acount rediscovery
    # latest_snapshot = asyncio.run( s_req.send_request(
    #     method=HTTPMethods.GET,
    #     resource=APIResources.START_DISCOVERY,
    #     response_model=str,
    #     branch=branch,
    #     uuid=account_id

    # ))
    latest_snapshot = 'f22718c8-457e-4418-8145-cfecabebad8f'
    # wait until snapshot is successfull
    asyncio.run(_is_snapshot_complete(snapshot_id=latest_snapshot, shared_secret=shared_secret,account_id=account_id))

    # Download report
    asyncio.run(print_report(account_id=account_id, shared_secret=shared_secret))



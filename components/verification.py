import feffery_antd_components as fac

from components.model import llm


def verify_DBRX_credentials():
    try:
        llm.invoke("")
        icon = fac.AntdIcon(icon="antd-check")
        danger = False

    except Exception as e:
        icon = fac.AntdIcon(icon="antd-close")
        danger = True
        print("Invalid DBRX credentials, add DBRX_API_KEY and DBRX_BASE_URL in .env file!")
    
    return fac.AntdButton(
        "⠀DBRX Token",
        icon=icon,
        id="token-button",
        type="text",
        size="medium",
        danger=danger
    )
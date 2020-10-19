from selenium.webdriver.common.by import By


class BaseActionsLocators:
    PROFILE_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div')
    LOGOUT_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/ul/li[2]/a')


class LoginPageLocators:
    MAIN_LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    EMAIL_FIELD = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    PASSWORD_FIELD = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    SUB_LOGIN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
    INCORRECT_EMAIL_OR_TEL_NUMBER__ELEMENT = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div')
    INVALID_LOGIN_OR_PASSWORD_ELEMENT = (By.XPATH, '//*[@id="login_form"]/div[1]/div/div[2]')

class CampaignsListPageLocators:
    PROFILE_ELEMENT = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[1]/a')
    FIRST_COMPANY_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div')
    TRAFFIC_GOAL_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]')
    LINK_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input')
    CAMPAIGN_NAME_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[9]/div/div[2]/div/div[2]/input')
    CLEAR_NAME_FIELD_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[9]/div/div[2]/div/div[1]')
    BUDGET_PER_DAY_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[3]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/div/input')
    BUDGET_TOTAL_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[3]/div/div[7]/ul/li[4]/li/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/input')
    BANNER_BUTTON = (By.XPATH, '//*[@id="patterns_4"]')
    IMG_DROP_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/input')
    SUBMIT_UPLOAD_BUTTON = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button/div')
    NEW_CAMPAIGN_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div')

    CHECKBOX_FOR_ALL_CAMPAIGNS = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div[1]/div/div[1]/div[3]/input')
    ACTIONS_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div[1]/span')
    DELETE_BUTTON = (By.XPATH, 'html/body/div[5]/div/div/div/div/ul/li[5]')

    CAMPAIGN_NAME_ELEM = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div/div[3]/div/a')

    SEGMENTS_BUTTON = (By.XPATH, '//html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[2]/a')


class SegmentsPageLocators:
    NEW_SEGMENT_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[4]')
    FIRST_SEGMENT_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div/ul/li[2]/a')
    ADD_AUDIENCE_SEGMENTS_BUTTON = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]')
    CHECKBOX1_1 = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/input')
    CHECKBOX1_2 = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/input')
    CHECKBOX2_1 = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/input')
    SUBMIT_CONFIGURE_SEGMENT_BUTTON = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[5]/div[1]/button')
    SEGMENT_NAME_FIELD = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/input')
    SUBMIT_CREATE_SEGMENT_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/button/div')

    SEGMENT_NAME_ELEM = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/a')

    CHECKBOX_FOR_ALL_SEGMENTS = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/div[3]/div/input')
    ACTIONS_BUTTON_SEG = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[5]/div[2]/div/div/div[1]/span')
    DELETE_BUTTON_SEG = (By.XPATH, '/html/body/div[6]/div/div/div/div/ul/li')
    DELETE_SEGMENT_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[6]/span')
    CONFIRM_DELETE_SEGMENT_BUTTON = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/div[2]/button[1]/div')

from behave import *

@given(u'User navigate to login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User navigate to login page')


@when(u'User enters valid username and valid password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters valid username and valid password')


@when(u'Click login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click login button')


@then(u'Proper message should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper message should be displayed')


@then(u'Proper error message should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper error message should be displayed')
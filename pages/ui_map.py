__author__ = 'Evgen'


class LoginPageMap(object):
    UsernameFieldId = "inputLogin"
    PasswordFieldId = "inputPassword"
    SubmitButtonXpath = "//button[@type='submit']"
    ThisPageName = "auth"


class PersonsPageMap(object):
    AddPersonButtonXpath = "//button[contains(@class,'btn-success')]"


class EnrollmentPageMap(object):
    pass


class InternalPageMap(object):
    pass


class NewPersonPageMap(object):
    ThisPageXpath = "//label[@for='inputDocSeries']"
    pass

# LoginPageMap = dict(UsernameFieldID="inputLogin"
#
#                     )
#
# PersonPageMap = dict(AddPersonButton="//button[contains(@class,'btn-success')]",
#
#                      )
#
# ApplicationPageMap = dict(QuantityDropDownID="wsite-com-product-option-Quantity",
#
#                           )
#
# InternalPageMap = dict(ShareLinkButtonName="share"
#                        )

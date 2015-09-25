__author__ = 'Evgen'


class LoginPageMap(object):
    UsernameFieldID = "inputLogin"
    PasswordFieldID = "inputPassword"
    SubmitButtonXPATH = "//button[@type='submit']"
    ThisPageNAME = "auth"


class PersonsPageMap(object):
    AddPersonButtonXPATH = "//button[contains(@class,'btn-success')]"


class EnrollmentPageMap(object):
    pass


class InternalPageMap(object):
    pass


class NewPersonPageMap(object):
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

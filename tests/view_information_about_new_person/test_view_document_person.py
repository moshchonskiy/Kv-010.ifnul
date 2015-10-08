# coding=utf-8
import time
from model.user import User

__author__ = 'Vadym'

def test_login_page_document_verify(app):
    app.ensure_logout()
    app.login(User.Admin())
    app.internal_page.is_this_page
    app.internal_page.driver.get('http://194.44.198.221/#/person/view/68/main')
    time.sleep(8)

    assert app.person_papers_view_page.get_text_person_profile() == u"Перегляд персони"
    app.person_main_view_page.person_document_button().click()
    time.sleep(2)

    assert app.person_papers_view_page.is_table_present() == True

# Нужно переделать логику, что бы ассерт был не по сортировке всех данных в таблице, а по строке.
# Так как есть вероятность что данные с разных строк пересекуться, но тест пройдет все равно
def test_verify_table_with_papers(app):
    data_table_papers = [u'Диплом', u'МА', u'19531209', u'2014-12-09', u'МАЛКОВИЧ', u'✓', u'✓',
            u'Всеукраїнські конкурси — захисти науково-дослідницьких робіт учнів - членів Малої академії наук України',
                         u'Педагогіка та психологія. Диплом I ступеня', u'', u'', u'',

                         u'Диплом магістра', u'АА', u'19530912', u'2015-05-05', u'Self', u'✓', u'✘', u'',
                         u'', u'З відзнакою', u'56', u'',

                         u'Сертифікат ЗНО', u'ММ', u'12091953', u'2015-06-01', u'Самовидано', u'✓', u'✘', u'',
                         u'', u'', u'', u'001122']

    count_documents = 3
    count_row_in_table = app.person_papers_view_page.get_count_row_in_table_documents()
    assert count_row_in_table == count_documents

    arr_info_from_table_web = app.person_papers_view_page.get_data_from_table()

    data_table_papers.sort()
    arr_info_from_table_web.sort()

    assert len(data_table_papers) == len(arr_info_from_table_web)

    for index, value_from_web in enumerate(arr_info_from_table_web):
        assert data_table_papers[index] == value_from_web
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface


class GetUserFormsInteractor:
    def __init__(self, form_storage: FormStorageInterface,
                 presenter: PresenterInterface):
        self.form_storage = form_storage
        self.presenter = presenter

    def get_user_forms(self, user_id: int):
        list_of_form_titles_with_id_dto = self.form_storage.get_user_forms(
            user_id=user_id
        )

        list_of_forms_dict = self.presenter.get_user_forms_response(
            list_of_form_titles_with_id_dto
        )
        return list_of_forms_dict

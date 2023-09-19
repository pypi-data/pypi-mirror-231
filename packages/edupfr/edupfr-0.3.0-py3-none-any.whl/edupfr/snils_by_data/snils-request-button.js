function () {
    var button = Ext.getCmp('{{ component.client_id }}');

    var snils_field = Ext.getCmp('{{ component.snils_field.client_id }}');

    var last_name_field = Ext.getCmp('{{ component.last_name_field.client_id }}');
    var first_name_field = Ext.getCmp('{{ component.first_name_field.client_id }}');
    var date_of_birth_field = Ext.getCmp('{{ component.date_of_birth_field.client_id }}');

    {% if component.patronymic_field %}
    var patronymic_field = Ext.getCmp('{{ component.patronymic_field.client_id }}');
    {% else %}
    var patronymic_field = null;
    {% endif %}

    {% if component.gender_field and component.gender_choices %}
    var gender_field = Ext.getCmp('{{ component.gender_field.client_id }}');
    var gender_choices = {{ component.gender_choices_json|safe }};
    {% else %}
    var gender_field = null;
    var gender_choices = null;
    {% endif %}

    {% if component.dul_number_field and component.dul_date_field %}
    var dul_number_field = Ext.getCmp('{{ component.dul_number_field.client_id }}');
    var dul_date_field = Ext.getCmp('{{ component.dul_date_field.client_id }}');
    {% else %}
    var dul_number_field = null;
    var dul_date_field = null;
    {% endif %}

    function checkField(field) {
        if (!field.getValue()) {
            Ext.Msg.alert('Не заполнено поле "' + field.fieldLabel + '"');
            return false;
        } else {
            return true;
        }
    }

    {# проверка заполнения обязательных полей #}
    var required_fields = [last_name_field, first_name_field, date_of_birth_field];
    for (var i = 0; i < required_fields.length; i++) {
        if (!checkField(required_fields[i]))
            return;
    }

    /*if (gender_field !== null && !checkField(gender_field)) {
        return;
    }*/

    {% comment %}
    Если заполнено поле с датой выдачи документа, удостоверяющего личность,
    то должен быть указан и номер документа.
    {% endcomment %}
    if (dul_date_field.getValue()) {
        if (!checkField(dul_number_field)) {
            return;
        }
    }

    {# подготовка параметров для HTTP-запроса #}
    var params = {
        'last_name': last_name_field.getValue(),
        'first_name': first_name_field.getValue(),
        'date_of_birth': date_of_birth_field.getValue().clearTime()
    }
    if (patronymic_field !== null)
        params['patronymic'] = patronymic_field.getValue();
    if (gender_field !== null)
        params['gender'] = gender_choices[gender_field.getValue()];
    if (dul_number_field !== null)
        params['dul_number'] = dul_number_field.getValue();
    if (dul_date_field !== null) {
        var dul_date = dul_date_field.getValue();
        if (dul_date)
            params['dul_date'] = dul_date.clearTime();
    }

    if (dul_number_field !== null)
        params['has_dul_fields'] = true;

    var requestId = Ext.Ajax.request({
        url: '{{ component.snils_request_action_url }}',
        params: params,
        success: function(response, options) {
            var result = Ext.util.JSON.decode(response.responseText);
            if (result.success) {
                snils_field.setValue(result.code);
            } else {
                Ext.Msg.alert('Ошибка', result.message);
            }
        },
        failure: function(response, options) {
            uiAjaxFailMessage(response, options);
        }
    });

    {# Отмена запроса при закрытии окна #}
    snils_field.on('beforedestroy', function () {
        if (Ext.Ajax.isLoading(requestId))
            Ext.Ajax.abort(requestId);

        return true;
    });
}

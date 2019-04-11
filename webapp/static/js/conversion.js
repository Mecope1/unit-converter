function conversionSetup(typeUnits, defaults){

    $(document).ready(function(){
        $(".unit-type-button").click(function(){
            $(".unit-type-button").removeClass('active');
            $(".unit-type-button").attr('aria-pressed', false);

            let currentButton = $(this);
            currentButton.addClass('active');
            currentButton.attr('aria-pressed', true);
            $(`#given_prefix`).val("");
            $(`#desired_prefix`).val("");

            let buttonName = currentButton.attr('value');

            $("#unit_type_input").attr("value", buttonName);


            let givenUnitSelect = $("#given_unit");
            givenUnitSelect.empty();
            givenUnitSelect.append("<option value=\"\" selected disabled>Select a unit</option>");

            for (let unitName of typeUnits[buttonName]){
                givenUnitSelect.append(`<option id="given-${buttonName}-${unitName}" value="${unitName}">${unitName}</option>`)
            }
            let desiredUnitSelect = $("#desired_unit");
            desiredUnitSelect.empty();
            desiredUnitSelect.append("<option value=\"\" selected disabled>Select a unit</option>");

            for (let unitName of typeUnits[buttonName]){
                desiredUnitSelect.append(`<option id="desired-${buttonName}-${unitName}" value="${unitName}">${unitName}</option>`)
            }
        });
        if(defaults) {
            $(`#btn-${defaults.unit_type}`).trigger("click");
            $(`#given_value`).val(defaults.given_num);
            $(`#given_prefix`).val(defaults.given_prefix);
            $(`#given_unit`).val(defaults.given_unit);
            $(`#desired_prefix`).val(defaults.desired_prefix);
            $(`#desired_unit`).val(defaults.desired_unit);
        }

    });
}


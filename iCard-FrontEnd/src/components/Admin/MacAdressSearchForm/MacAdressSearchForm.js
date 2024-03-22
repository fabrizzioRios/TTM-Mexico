import React from 'react';
import './MacAdressSearchForm.scss'
import {useFormik} from "formik";
import * as Yup from "yup";
import {Button, Form} from "semantic-ui-react";
import {searchMacAddressApi} from "../../../api/connections";

export function MacAdressSearchForm() {

    const formik = useFormik({
        initialValues: InitialValues(),
        validationSchema: newValidationSchema(),
        validateOnChange: false,
        onSubmit: async (formValues) => {
            try {
                const response = await searchMacAddressApi(formValues)
                console.log(response)
            } catch (error) {
                console.log(error);
            }
        }
    });

    return (
        <Form className={"search_mac_address_form"} onSubmit={formik.handleSubmit}>
            <Form.Input
                name={"mac_address"}
                placeholder={"Introduce the device mac address"}
                value={formik.values.mac_address}
                onChange={formik.handleChange}
                error={formik.errors.mac_address}
            />
            <Button type={"submit"} content={"Send"} primary fluid/>
        </Form>
    );
}

function InitialValues() {
    return {
        mac_address: "",
    };
}

function newValidationSchema() {
    return Yup.object({
        mac_address: Yup.string(),
    });
}


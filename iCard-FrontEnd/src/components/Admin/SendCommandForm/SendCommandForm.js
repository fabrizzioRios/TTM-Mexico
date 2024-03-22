import React from 'react';
import { Button, Checkbox, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
import './SendCommandForm.scss';
import { sendCommandDeviceApi } from "../../../api/connections";

export function SendCommandForm(props) {
    const { nd_switch } = props

    const formik = useFormik({
        initialValues: InitialValues(),
        validationSchema: newValidationSchema(),
        validateOnChange: false,
        onSubmit: async (formValues) => {
            try {
                const formData = new FormData();
                formData.append('writed_command', formValues.writed_command);
                formData.append('access_mode', formValues.access_mode);
                formData.append('enable_mode', formValues.enable_mode);
                formData.append('conf_mode', formValues.conf_mode);
                formData.append('from_file', formValues.from_file);
                formData.append('file', formValues.file);
                formData.append('device_data', JSON.stringify(nd_switch));

                const response = await sendCommandDeviceApi(formData);

                console.log(response)
            } catch (error) {
                console.log(error);
            }
        }
    });

    return (
        <Form className={"send_command_form"} onSubmit={formik.handleSubmit}>
            <Form.Input
                name={"writed_command"}
                placeholder={"Write your command"}
                value={formik.values.writed_command}
                onChange={formik.handleChange}
                error={formik.errors.writed_command}
                disabled={formik.values.from_file} // Disable only when "from_file" checkbox is checked
                className={formik.values.from_file ? "disabled-input" : ""} // Add a class when disabled
            />
            <div className={"send_command_form_enable_mode"}>
                <Checkbox
                    toggle
                    checked={formik.values.enable_mode}
                    onChange={(_, data) => {
                        formik.setFieldValue('enable_mode', data.checked);
                        if (data.checked) {
                            formik.setFieldValue('conf_mode', false);
                            formik.setFieldValue('from_file', false);
                        }
                    }}
                /> Enable mode
            </div>
            <div className={"send_command_form_enable_mode"}>
                <Checkbox
                    toggle
                    checked={formik.values.conf_mode}
                    onChange={(_, data) => {
                        formik.setFieldValue('conf_mode', data.checked);
                        if (data.checked) {
                            formik.setFieldValue('enable_mode', false);
                            formik.setFieldValue('from_file', false);
                        }
                    }}
                /> Config mode
            </div>
            <div className={"send_command_form_from_file"}>
                <Checkbox
                    toggle
                    checked={formik.values.from_file}
                    onChange={(_, data) => {
                        formik.setFieldValue('from_file', data.checked);
                        if (data.checked) {
                            formik.setFieldValue('enable_mode', false);
                            formik.setFieldValue('conf_mode', false);
                        }
                    }}
                /> Send command from file
            </div>
            {formik.values.from_file && (
                <div className={"dropbox-container"}>
                    <label
                        htmlFor="file-input"
                        className={"send_command_form_from_file dropbox"}
                        onDrop={(event) => {
                            event.preventDefault();
                            const file = event.dataTransfer.files[0];
                            formik.setFieldValue('file', file);
                        }}
                        onDragOver={(event) => {
                            event.preventDefault();
                        }}
                    >
                        <p>{formik.values.file ? formik.values.file.name : "Drop file here or click to upload"}</p>
                        <input
                            id="file-input"
                            type="file"
                            style={{ display: 'none' }}
                            onChange={(event) => {
                                const file = event.currentTarget.files[0];
                                formik.setFieldValue('file', file);
                            }}
                        />
                    </label>
                </div>
            )}
            <Button type={"submit"} content={"Send"} primary fluid/>
        </Form>
    );
}

function InitialValues() {
    return {
        writed_command: "",
        access_mode: true,
        enable_mode: false,
        conf_mode: false,
        from_file: false,
        file: null
    };
}

function newValidationSchema() {
    return Yup.object({
        writed_command: Yup.string(),
        access_mode: Yup.bool(),
        enable_mode: Yup.bool(),
        conf_mode: Yup.bool(),
        from_file: Yup.bool(),
        file: Yup.mixed()  // Use Yup mixed type for file
    });
}
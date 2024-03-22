import { BASE_API } from "../utils/constants";

export async function runBGPScript(formValue) {
    try {
        const url = `${BASE_API}/api/v1/bgp-script-run/13`;
        const params = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formValue)
        };

        const response = await fetch(url, params)

        if(response.status !== 200) {
            throw new Error("Error")
        }
        const result = await response.json();
        console.log(result)
        return result
    } catch (error) {
        throw error
    }
}
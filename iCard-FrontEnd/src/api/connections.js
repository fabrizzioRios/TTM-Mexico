import {BASE_API} from "../utils/constants";

export async function runPingApi(data) {
    try {
        const url = `${BASE_API}/network_api/ping/`;
        const params = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };

        const response = await fetch(url, params)
        return await response.json()
    } catch (error) {
        throw error
    }
}

export async function sshConnectDeviceApi(data) {
    try {
        const url = `${BASE_API}/network_api/ssh-connection/`;
        const params = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };

        const response = await fetch(url, params)
        return await response.json()
    } catch (error) {
        throw error
    }
}

export async function sendCommandDeviceApi(data) {
    try {
        const url = `${BASE_API}/network_api/send-command/`;
        const params = {
            method: "POST",
            body: data
        };

        const response = await fetch(url, params);
        return await response.json();
    } catch (error) {
        throw error;
    }
}

export async function searchMacAddressApi(data) {
    try {
        const url = `${BASE_API}/network_api/search-mac/`;
        const params = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };

        const response = await fetch(url, params)
        return await response.json()
    } catch (error) {
        throw error
    }
}
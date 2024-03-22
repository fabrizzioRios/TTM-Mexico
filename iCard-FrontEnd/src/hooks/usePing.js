import {useState} from "react";
import {useAuth} from "./useAuth";
import {runPingApi} from "../api/connections";

export function usePing() {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [ping, setPing] = useState(null);
    const {auth} = useAuth();

    const getPing = async () => {
        try {
            setLoading(true)
            const response = await runPingApi(auth.token)
            setLoading(false)
            setPing(response)
        } catch (error) {
            setLoading(false)
            setError(error)
        }
    }
    return {
        loading,
        error,
        ping,
        getPing
    }
}
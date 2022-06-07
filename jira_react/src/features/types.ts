import { Tracing } from "trace_events";

/** authSlice.ts */
export interface LOGIN_USER {
    id: number;
    username: string;
}

export interface FILE extends Blob {
    readonly lastModified: number;
    readonly name: Tracing;
}

export interface PROFILE {
    id: number;
    user_prefile: number;
    img: string | null;
}

export interface POST_PROFILE {
    id: number;
    img: File | null;
}

export interface CRED {
    username: string;
    password: string;
}

export interface JWT {
    refresh: string;
    access: string;
}

export interface USER {
    id: number;
    username: string;
}

export interface AUTH_STATE {
    isLoginView: boolean;
    loginUser: LOGIN_USER;
    profiles: PROFILE[];
}

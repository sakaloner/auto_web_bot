
// this file is generated — do not edit it


/// <reference types="@sveltejs/kit" />

/**
 * Environment variables [loaded by Vite](https://vitejs.dev/guide/env-and-mode.html#env-files) from `.env` files and `process.env`. Like [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), this module cannot be imported into client-side code. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env).
 * 
 * _Unlike_ [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), the values exported from this module are statically injected into your bundle at build time, enabling optimisations like dead code elimination.
 * 
 * ```ts
 * import { API_KEY } from '$env/static/private';
 * ```
 * 
 * Note that all environment variables referenced in your code should be declared (for example in an `.env` file), even if they don't have a value until the app is deployed:
 * 
 * ```
 * MY_FEATURE_FLAG=""
 * ```
 * 
 * You can override `.env` values from the command line like so:
 * 
 * ```bash
 * MY_FEATURE_FLAG="enabled" npm run dev
 * ```
 */
declare module '$env/static/private' {
	export const SHELL: string;
	export const npm_command: string;
	export const LSCOLORS: string;
	export const USER_ZDOTDIR: string;
	export const npm_config_userconfig: string;
	export const COLORTERM: string;
	export const npm_config_cache: string;
	export const LESS: string;
	export const NVM_INC: string;
	export const TERM_PROGRAM_VERSION: string;
	export const WLR_NO_HARDWARE_CURSORS: string;
	export const WLR_RENDERER_ALLOW_SOFTWARE: string;
	export const QT_WAYLAND_DISABLE_WINDOWDECORATION: string;
	export const I3SOCK: string;
	export const _P9K_TTY: string;
	export const NODE: string;
	export const LESS_TERMCAP_se: string;
	export const LESS_TERMCAP_so: string;
	export const LC_ADDRESS: string;
	export const LC_NAME: string;
	export const P9K_TTY: string;
	export const COLOR: string;
	export const npm_config_local_prefix: string;
	export const LC_MONETARY: string;
	export const MOZ_DBUS_REMOTE: string;
	export const NO_AT_BRIDGE: string;
	export const npm_config_globalconfig: string;
	export const XCURSOR_SIZE: string;
	export const EDITOR: string;
	export const XDG_SEAT: string;
	export const PWD: string;
	export const XDG_VIDEOS_DIR: string;
	export const LOGNAME: string;
	export const QT_QPA_PLATFORMTHEME: string;
	export const XDG_SESSION_TYPE: string;
	export const npm_config_init_module: string;
	export const PKGFILE_PROMPT_INSTALL_MISSING: string;
	export const _: string;
	export const XDG_PICTURES_DIR: string;
	export const LS_OPTIONS: string;
	export const VSCODE_GIT_ASKPASS_NODE: string;
	export const ZEIT_DB: string;
	export const Path: string;
	export const MOTD_SHOWN: string;
	export const VSCODE_INJECTION: string;
	export const HOME: string;
	export const XDG_PUBLICSHARE_DIR: string;
	export const LC_PAPER: string;
	export const LANG: string;
	export const LS_COLORS: string;
	export const _JAVA_AWT_WM_NONREPARENTING: string;
	export const XDG_CURRENT_DESKTOP: string;
	export const npm_package_version: string;
	export const VIRTUAL_ENV: string;
	export const SWAYSOCK: string;
	export const WAYLAND_DISPLAY: string;
	export const TERMINAL_COMMAND: string;
	export const XDG_DOWNLOAD_DIR: string;
	export const GIT_ASKPASS: string;
	export const XDG_MUSIC_DIR: string;
	export const XDG_TEMPLATES_DIR: string;
	export const GTK_CSD: string;
	export const INIT_CWD: string;
	export const CHROME_DESKTOP: string;
	export const QT_QPA_PLATFORM: string;
	export const npm_lifecycle_script: string;
	export const NVM_DIR: string;
	export const VSCODE_GIT_ASKPASS_EXTRA_ARGS: string;
	export const XDG_ACTIVATION_TOKEN: string;
	export const XDG_SESSION_CLASS: string;
	export const XDG_DESKTOP_DIR: string;
	export const LC_IDENTIFICATION: string;
	export const TERM: string;
	export const npm_package_name: string;
	export const LESS_TERMCAP_mb: string;
	export const LESS_TERMCAP_me: string;
	export const LESS_TERMCAP_md: string;
	export const npm_config_prefix: string;
	export const ZDOTDIR: string;
	export const USER: string;
	export const VSCODE_GIT_IPC_HANDLE: string;
	export const DISPLAY: string;
	export const npm_lifecycle_event: string;
	export const LESS_TERMCAP_ue: string;
	export const SHLVL: string;
	export const NVM_CD_FLAGS: string;
	export const MOZ_ENABLE_WAYLAND: string;
	export const LESS_TERMCAP_us: string;
	export const PAGER: string;
	export const LC_TELEPHONE: string;
	export const _P9K_SSH_TTY: string;
	export const LC_MEASUREMENT: string;
	export const XDG_VTNR: string;
	export const XDG_SESSION_ID: string;
	export const VIRTUAL_ENV_PROMPT: string;
	export const npm_config_user_agent: string;
	export const npm_execpath: string;
	export const XDG_RUNTIME_DIR: string;
	export const DEBUGINFOD_URLS: string;
	export const npm_package_json: string;
	export const LC_TIME: string;
	export const WLR_DRM_NO_MODIFIERS: string;
	export const XDG_DOCUMENTS_DIR: string;
	export const GREETD_SOCK: string;
	export const P9K_SSH: string;
	export const VSCODE_GIT_ASKPASS_MAIN: string;
	export const GDK_BACKEND: string;
	export const npm_config_noproxy: string;
	export const PATH: string;
	export const XDG_SCREENSHOTS_DIR: string;
	export const npm_config_metrics_registry: string;
	export const npm_config_node_gyp: string;
	export const ORIGINAL_XDG_CURRENT_DESKTOP: string;
	export const DBUS_SESSION_BUS_ADDRESS: string;
	export const npm_config_global_prefix: string;
	export const NVM_BIN: string;
	export const MAIL: string;
	export const npm_node_execpath: string;
	export const npm_config_engine_strict: string;
	export const LC_NUMERIC: string;
	export const OLDPWD: string;
	export const TERM_PROGRAM: string;
	export const LIBSEAT_BACKEND: string;
	export const NODE_ENV: string;
}

/**
 * Similar to [`$env/static/private`](https://kit.svelte.dev/docs/modules#$env-static-private), except that it only includes environment variables that begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Values are replaced statically at build time.
 * 
 * ```ts
 * import { PUBLIC_BASE_URL } from '$env/static/public';
 * ```
 */
declare module '$env/static/public' {
	
}

/**
 * This module provides access to runtime environment variables, as defined by the platform you're running on. For example if you're using [`adapter-node`](https://github.com/sveltejs/kit/tree/master/packages/adapter-node) (or running [`vite preview`](https://kit.svelte.dev/docs/cli)), this is equivalent to `process.env`. This module only includes variables that _do not_ begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env).
 * 
 * This module cannot be imported into client-side code.
 * 
 * ```ts
 * import { env } from '$env/dynamic/private';
 * console.log(env.DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 * 
 * > In `dev`, `$env/dynamic` always includes environment variables from `.env`. In `prod`, this behavior will depend on your adapter.
 */
declare module '$env/dynamic/private' {
	export const env: {
		SHELL: string;
		npm_command: string;
		LSCOLORS: string;
		USER_ZDOTDIR: string;
		npm_config_userconfig: string;
		COLORTERM: string;
		npm_config_cache: string;
		LESS: string;
		NVM_INC: string;
		TERM_PROGRAM_VERSION: string;
		WLR_NO_HARDWARE_CURSORS: string;
		WLR_RENDERER_ALLOW_SOFTWARE: string;
		QT_WAYLAND_DISABLE_WINDOWDECORATION: string;
		I3SOCK: string;
		_P9K_TTY: string;
		NODE: string;
		LESS_TERMCAP_se: string;
		LESS_TERMCAP_so: string;
		LC_ADDRESS: string;
		LC_NAME: string;
		P9K_TTY: string;
		COLOR: string;
		npm_config_local_prefix: string;
		LC_MONETARY: string;
		MOZ_DBUS_REMOTE: string;
		NO_AT_BRIDGE: string;
		npm_config_globalconfig: string;
		XCURSOR_SIZE: string;
		EDITOR: string;
		XDG_SEAT: string;
		PWD: string;
		XDG_VIDEOS_DIR: string;
		LOGNAME: string;
		QT_QPA_PLATFORMTHEME: string;
		XDG_SESSION_TYPE: string;
		npm_config_init_module: string;
		PKGFILE_PROMPT_INSTALL_MISSING: string;
		_: string;
		XDG_PICTURES_DIR: string;
		LS_OPTIONS: string;
		VSCODE_GIT_ASKPASS_NODE: string;
		ZEIT_DB: string;
		Path: string;
		MOTD_SHOWN: string;
		VSCODE_INJECTION: string;
		HOME: string;
		XDG_PUBLICSHARE_DIR: string;
		LC_PAPER: string;
		LANG: string;
		LS_COLORS: string;
		_JAVA_AWT_WM_NONREPARENTING: string;
		XDG_CURRENT_DESKTOP: string;
		npm_package_version: string;
		VIRTUAL_ENV: string;
		SWAYSOCK: string;
		WAYLAND_DISPLAY: string;
		TERMINAL_COMMAND: string;
		XDG_DOWNLOAD_DIR: string;
		GIT_ASKPASS: string;
		XDG_MUSIC_DIR: string;
		XDG_TEMPLATES_DIR: string;
		GTK_CSD: string;
		INIT_CWD: string;
		CHROME_DESKTOP: string;
		QT_QPA_PLATFORM: string;
		npm_lifecycle_script: string;
		NVM_DIR: string;
		VSCODE_GIT_ASKPASS_EXTRA_ARGS: string;
		XDG_ACTIVATION_TOKEN: string;
		XDG_SESSION_CLASS: string;
		XDG_DESKTOP_DIR: string;
		LC_IDENTIFICATION: string;
		TERM: string;
		npm_package_name: string;
		LESS_TERMCAP_mb: string;
		LESS_TERMCAP_me: string;
		LESS_TERMCAP_md: string;
		npm_config_prefix: string;
		ZDOTDIR: string;
		USER: string;
		VSCODE_GIT_IPC_HANDLE: string;
		DISPLAY: string;
		npm_lifecycle_event: string;
		LESS_TERMCAP_ue: string;
		SHLVL: string;
		NVM_CD_FLAGS: string;
		MOZ_ENABLE_WAYLAND: string;
		LESS_TERMCAP_us: string;
		PAGER: string;
		LC_TELEPHONE: string;
		_P9K_SSH_TTY: string;
		LC_MEASUREMENT: string;
		XDG_VTNR: string;
		XDG_SESSION_ID: string;
		VIRTUAL_ENV_PROMPT: string;
		npm_config_user_agent: string;
		npm_execpath: string;
		XDG_RUNTIME_DIR: string;
		DEBUGINFOD_URLS: string;
		npm_package_json: string;
		LC_TIME: string;
		WLR_DRM_NO_MODIFIERS: string;
		XDG_DOCUMENTS_DIR: string;
		GREETD_SOCK: string;
		P9K_SSH: string;
		VSCODE_GIT_ASKPASS_MAIN: string;
		GDK_BACKEND: string;
		npm_config_noproxy: string;
		PATH: string;
		XDG_SCREENSHOTS_DIR: string;
		npm_config_metrics_registry: string;
		npm_config_node_gyp: string;
		ORIGINAL_XDG_CURRENT_DESKTOP: string;
		DBUS_SESSION_BUS_ADDRESS: string;
		npm_config_global_prefix: string;
		NVM_BIN: string;
		MAIL: string;
		npm_node_execpath: string;
		npm_config_engine_strict: string;
		LC_NUMERIC: string;
		OLDPWD: string;
		TERM_PROGRAM: string;
		LIBSEAT_BACKEND: string;
		NODE_ENV: string;
		[key: `PUBLIC_${string}`]: undefined;
		[key: string]: string | undefined;
	}
}

/**
 * Similar to [`$env/dynamic/private`](https://kit.svelte.dev/docs/modules#$env-dynamic-private), but only includes variables that begin with [`config.kit.env.publicPrefix`](https://kit.svelte.dev/docs/configuration#env) (which defaults to `PUBLIC_`), and can therefore safely be exposed to client-side code.
 * 
 * Note that public dynamic environment variables must all be sent from the server to the client, causing larger network requests — when possible, use `$env/static/public` instead.
 * 
 * ```ts
 * import { env } from '$env/dynamic/public';
 * console.log(env.PUBLIC_DEPLOYMENT_SPECIFIC_VARIABLE);
 * ```
 */
declare module '$env/dynamic/public' {
	export const env: {
		[key: `PUBLIC_${string}`]: string | undefined;
	}
}

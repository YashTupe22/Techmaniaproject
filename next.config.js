/** @type {import('next').NextConfig} */
const nextConfig = {
    webpack: (config) => {
        // Support for WASM files (MediaPipe)
        config.experiments = {
            ...config.experiments,
            asyncWebAssembly: true,
        };

        config.module.rules.push({
            test: /\.wasm$/,
            type: 'webassembly/async',
        });

        return config;
    },
    // Enable static export for Vercel
    output: 'standalone',
};

module.exports = nextConfig;

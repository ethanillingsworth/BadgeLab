import path from "path";
import { fileURLToPath } from "url";
import HtmlWebpackPlugin from "html-webpack-plugin";
import MiniCssExtractPlugin from "mini-css-extract-plugin";
import CopyWebpackPlugin from "copy-webpack-plugin";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default {
	entry: ["./src/index.js"],
	mode: "development",
	experiments: {
		topLevelAwait: true,
	},
	output: {
		path: path.resolve(__dirname, "public"),
		filename: "[name].js",
		assetModuleFilename: "imgs/[hash][ext][query]",
		clean: true,
		publicPath: "/",
	},
	module: {
		rules: [
			{
				test: /\.css$/i,
				use: [
					MiniCssExtractPlugin.loader,
					"css-loader",
					"postcss-loader",
				],
			},
			{
				test: /\.(png|jpe?g|gif|svg|webp)$/i,
				type: "asset/resource", // emits a separate file and exports the URL
			},
		],
	},
	devServer: {
		static: {
			directory: path.join(__dirname, "public"),
		},
		compress: true,
		port: 5500, // you can change this port
		open: true, // auto-opens the browser
		hot: true, // enables hot module replacement
		liveReload: true, // fallback auto-reload if HMR fails
	},
	plugins: [
		new MiniCssExtractPlugin({
			filename: "index.css",
		}),
		new CopyWebpackPlugin({
			patterns: [
				{
					from: "src/netlify.toml", // where you put the _redirects file
					to: "", // output it at the root of /public
				},
				{
					from: "src/netlify/",
					to: "netlify",
				},
				{
					from: "src/icons/",
					to: "icons",
				},
				{
					from: "README.md",
					to: "",
				},
				{
					from: "badgelist.json",
					to: "",
				},
			],
		}),
		new HtmlWebpackPlugin({
			template: "./src/index.html",
			filename: "index.html",
			chunks: ["main"],
			// favicon: "./src/imgs/logo.png",
		}),
	],
};

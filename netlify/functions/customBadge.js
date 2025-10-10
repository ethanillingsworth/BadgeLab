import fs from "fs";
import path from "path";

export async function handler(event, context) {
	const params = new URLSearchParams(event.rawQuery || "");
	const name = params.get("name");
	const textColor = params.get("textColor") || "white";
	const bgColor = params.get("bgColor");
	const scale = 16;
	const image = params.get("image") || "null";
	const noLogo = params.get("noLogo") || false;

	const styles = `
	<style>
		text {
			text-transform: uppercase;
		}
	</style>`;

	let e = `<svg width="${
		name.length * scale * 0.6 + 20
	}" height="40" xmlns="http://www.w3.org/2000/svg">
		${styles}
		<rect fill="#${bgColor}" x="0" y="0" rx="8" ry="8" width="100%" height="40" />
		<text x="10" y="22" font-weight="bold" font-family="monospace" font-size="${scale}" fill="#${textColor}" dominant-baseline="middle" text-anchor="left">
			${name}
		</text>
	</svg>`;

	if (
		!image.endsWith("undefined") &&
		!image.endsWith("null") &&
		noLogo == "false"
	) {
		const response = await fetch(`${image}`);
		const svgData = await response.text();

		// Extract the viewBox values
		const viewBoxMatch = svgData.match(/viewBox="([\d.\s-]+)"/);
		let viewBox = [0, 0, 100, 100]; // fallback if missing
		if (viewBoxMatch) viewBox = viewBoxMatch[1].split(/\s+/).map(Number);

		// Strip the outer <svg> tags so we only keep its contents
		const innerSvg = svgData
			.replace(/<\?xml.*?\?>/, "")
			.replace(/<!DOCTYPE.*?>/, "")
			.replace(/<svg[^>]*>/, "")
			.replace(/<\/svg>/, "");

		// Normalize scaling based on viewBox
		const [minX, minY, vbWidth, vbHeight] = viewBox;
		const targetSize = 20; // desired size for all icons
		const scaleFactor = targetSize / Math.max(vbWidth, vbHeight);
		const offsetX = -minX * scaleFactor;
		const offsetY = -minY * scaleFactor;

		// Build the final badge SVG
		e = `<svg width="${
			name.length * scale * 0.6 + 55
		}" height="40" xmlns="http://www.w3.org/2000/svg">
			${styles}
			<rect fill="#${bgColor}" x="0" y="0" rx="8" ry="8" width="100%" height="40" />
			<g transform="translate(12.5,10) scale(${scaleFactor}) translate(${offsetX},${offsetY})">
				${innerSvg}
			</g>
			<text x="40" y="22" font-weight="bold" font-family="monospace" font-size="${scale}" fill="#${textColor}" dominant-baseline="middle" text-anchor="left">
				${name}
			</text>
		</svg>`;
	}

	return {
		statusCode: 200,
		headers: { "Content-Type": "image/svg+xml", "Cache-Control": "public, max-age=3600" },
		body: e,
	};
}

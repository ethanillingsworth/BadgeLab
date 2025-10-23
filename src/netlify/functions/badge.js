export async function handler(event, context) {
	const path = event.path; // e.g. "/function/hello"
	const params = new URLSearchParams(event.rawQuery || "");

	let name = path.split("/")[3];
	const noLogo = params.get("noLogo") || false;


	const badgeLookup = await (
		await fetch(`${process.env.URL}/badgeList.json`)
	).json();

	let badgeData;
	for (const cate of Object.keys(badgeLookup)) {

		badgeData = badgeLookup[cate][name] || null
		if (badgeData != null) {
			break
		}
	}


	if (badgeData == null) {
		return {
			statusCode: 404,
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				error: `Unable to find badge with id ${name}`,
			}),
		};
	}

	const response = await fetch(
		`${process.env.URL}/api/customBadge?name=${badgeData.name}&textColor=${badgeData.textColor}&bgColor=${badgeData.bgColor}&image=${process.env.URL}${badgeData.image}&noLogo=${noLogo}`
	);

	const data = await response.text();

	return {
		statusCode: 200,
		headers: { "Content-Type": "image/svg+xml", "Cache-Control": "public, max-age=3600" },
		body: data,
	};
}

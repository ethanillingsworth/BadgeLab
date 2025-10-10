export async function handler(event, context) {
	const path = event.path; // e.g. "/function/hello"
	const params = new URLSearchParams(event.rawQuery || "");

	const name = path.split("/").pop();
	const noLogo = params.get("noLogo") || false;

	const badgeLookup = await (
		await fetch(`${process.env.URL}/badgeList.json`)
	).json();

	const badgeData = badgeLookup[name] || null;

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
		headers: { "Content-Type": "image/svg+xml" },

		body: data,
	};
}

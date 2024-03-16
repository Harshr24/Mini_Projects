const jobs = [
    { title: "Frontend Developer", skills: ["html", "css", "javascript"] },
    { title: "Backend Developer", skills: ["nodejs", "express", "mongodb"] },
    { title: "Full Stack Developer", skills: ["html", "css", "javascript", "nodejs", "express", "mongodb"] },
    { title: "Data Scientist", skills: ["python", "machine learning", "data analysis"] },
    { title: "UX/UI Designer", skills: ["ui/ux design", "adobe xd", "figma"] },
    { title: "DevOps Engineer", skills: ["aws", "docker", "kubernetes"] }
];

function matchSkills() {
    const userSkillsInput = document.getElementById("skills").value.trim().toLowerCase().split(",");
    const matchingJobs = [];

    if (userSkillsInput.length === 0) {
        alert("Please enter your skills!");
        return;
    }

    jobs.forEach(job => {
        const jobSkills = job.skills.map(skill => skill.toLowerCase());
        const commonSkills = userSkillsInput.filter(skill => jobSkills.includes(skill));
        if (commonSkills.length > 0) {
            matchingJobs.push({ title: job.title, commonSkills });
        }
    });

    displayMatchingJobs(matchingJobs);
}

function displayMatchingJobs(matchingJobs) {
    const matchingJobsContainer = document.getElementById("matchingJobs");

    if (matchingJobs.length === 0) {
        matchingJobsContainer.innerHTML = "No matching jobs found.";
    } else {
        matchingJobsContainer.innerHTML = "";
        matchingJobs.forEach(job => {
            const jobElement = document.createElement("div");
            jobElement.innerHTML = `<strong>${job.title}</strong>: Matching Skills - ${job.commonSkills.join(", ")}`;
            matchingJobsContainer.appendChild(jobElement);
        });
    }
}

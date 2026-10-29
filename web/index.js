
const API_URL = "/problems/generate";

const generateButton = document.getElementById("generate");
const buttonText = document.getElementById("button-text");

const resultCard = document.getElementById("result-card");
const problemText = document.getElementById("problem-text");
const problemNumber = document.getElementById("problem-number");

const answerToggle = document.getElementById("answer-toggle");
const answerLabel = document.getElementById("answer-label");
const answerArrow = document.getElementById("answer-arrow");
const answerBox = document.getElementById("answer-box");
const answerText = document.getElementById("answer-text");

const errorBox = document.getElementById("error-box");
const errorText = document.getElementById("error-text");

const nextProblemButton = document.getElementById("next-problem");
const retryButton = document.getElementById("retry");

let problemCount = 0;
let currentAnswer = null;

async function generateProblem() {
    generateButton.disabled = true;
    buttonText.textContent = "در حال ساخت مسئله...";

    errorBox.classList.add("hidden");

    try {
        const response = await fetch(API_URL, {
            method: "POST"
        });

        if (!response.ok) {
            throw new Error(`خطای سرور: ${response.status}`);
        }

        const data = await response.json();

        if (
            typeof data.problem !== "string" ||
            !data.answer ||
            typeof data.answer !== "object"
        ) {
            throw new Error("ساختار پاسخ سرور معتبر نیست.");
        }

        problemCount++;
        currentAnswer = data.answer;

        problemText.textContent = data.problem;
        problemNumber.textContent = `مسئله ${problemCount}`;

        answerText.textContent = "";
        answerBox.classList.add("hidden");

        answerLabel.textContent = "نمایش پاسخ";
        answerArrow.textContent = "⌄";

        resultCard.classList.remove("hidden");

        resultCard.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });

    } catch (error) {
        errorText.textContent =
            `${error.message} — مطمئن شو سرور Python روشن است.`;

        errorBox.classList.remove("hidden");

        console.error("خطا در ساخت مسئله:", error);

    } finally {
        generateButton.disabled = false;
        buttonText.textContent = "ساخت مسئله جدید";
    }
}

function toggleAnswer() {
    if (!currentAnswer) {
        return;
    }

    const isHidden = answerBox.classList.contains("hidden");

    if (isHidden) {
        const answerLabels = {
            "اسب": "تعداد اسب‌ها",
            "خروس": "تعداد خروس‌ها",
            "گاو": "تعداد گاوها",
            "هشت‌پا": "تعداد هشت‌پاها",
            "گوسفند": "تعداد گوسفندها",
            "گربه": "تعداد گربه‌ها",
            "عنکبوت": "تعداد عنکبوت‌ها",
            "لاک‌پشت": "تعداد لاک‌پشت‌ها",
            "اردک": "تعداد اردک‌ها",
            "سگ": "تعداد سگ‌ها",
            "خرگوش": "تعداد خرگوش‌ها",
            "بوقلمون": "تعداد بوقلمون‌ها",
            "شیر": "تعداد شیرها",
            "فیل": "تعداد فیل‌ها",
            "میمون": "تعداد میمون‌ها",
            "قورباغه": "تعداد قورباغه‌ها",
            "مورچه": "تعداد مورچه‌ها",
            "زنبور": "تعداد زنبورها",
            "عقرب": "تعداد عقرب‌ها",
            "خرچنگ": "تعداد خرچنگ‌ها",
            "پنگوئن": "تعداد پنگوئن‌ها",
            "کانگورو": "تعداد کانگوروها",
            "تمساح": "تعداد تمساح‌ها",
            "دایناسور": "تعداد دایناسورها"
        };

        const answerLines = Object.entries(currentAnswer).map(
            ([key, value]) => {
                const label = answerLabels[key] || key;
                return `${label}: ${value}`;
            }
        );

        answerText.textContent = answerLines.join(" | ");

        answerBox.classList.remove("hidden");
        answerLabel.textContent = "پنهان کردن پاسخ";
        answerArrow.textContent = "⌃";

    } else {
        answerBox.classList.add("hidden");
        answerLabel.textContent = "نمایش پاسخ";
        answerArrow.textContent = "⌄";
    }
}

generateButton.addEventListener("click", generateProblem);
nextProblemButton.addEventListener("click", generateProblem);
answerToggle.addEventListener("click", toggleAnswer);
retryButton.addEventListener("click", generateProblem);

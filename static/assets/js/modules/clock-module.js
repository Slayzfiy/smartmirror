// CLOCK DRAW FUNCTIONS
function drawFace(ctx, radius, background_color) {
    let grad;
    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, 2 * Math.PI);
    ctx.fillStyle = background_color;
    ctx.fill();
    grad = ctx.createRadialGradient(0, 0, radius * 0.95, 0, 0, radius * 1.05);

    ctx.strokeStyle = grad;
    ctx.lineWidth = radius * 0.1;
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.1, 0, 2 * Math.PI);
    ctx.fillStyle = '#333';
    ctx.fill();
}
function drawNumbers(ctx, radius, numberColor) {
    let ang;
    let num;
    ctx.font = radius * 0.15 + "px arial";
    ctx.fillStyle = numberColor;
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";

    for (num = 1; num < 13; num++) {
        ang = num * Math.PI / 6;
        ctx.rotate(ang);
        ctx.translate(0, -radius * 0.85);
        ctx.rotate(-ang);
        ctx.fillText(num.toString(), 0, 0);
        ctx.rotate(ang);
        ctx.translate(0, radius * 0.85);
        ctx.rotate(-ang);
    }
}
function calcTime(offset) {
    let d = new Date();
    let utc = d.getTime() + (d.getTimezoneOffset() * 60000);
    return new Date(utc + (3600000 * offset));
}
function drawTime(ctx, radius, pointerColor, timezone) {
    let now = calcTime(parseInt(timezone) + 1)
    let hour = now.getHours();
    let minute = now.getMinutes();
    let second = now.getSeconds();
    hour = hour % 12;
    hour = (hour * Math.PI / 6) +
        (minute * Math.PI / (6 * 60)) +
        (second * Math.PI / (360 * 60));
    drawHand(ctx, hour, radius * 0.5, radius * 0.03, pointerColor);
    minute = (minute * Math.PI / 30) + (second * Math.PI / (30 * 60));
    drawHand(ctx, minute, radius * 0.75, radius * 0.05, pointerColor);
    second = (second * Math.PI / 30);
    drawHand(ctx, second, radius * 0.9, radius * 0.02, pointerColor);
}
function drawHand(ctx, pos, length, width, pointerColor) {
    ctx.beginPath();
    ctx.lineWidth = width;
    ctx.strokeStyle = pointerColor;
    ctx.lineCap = "round";
    ctx.moveTo(0, 0);
    ctx.rotate(pos);
    ctx.lineTo(0, -length);
    ctx.stroke();
    ctx.rotate(-pos);
}
// END
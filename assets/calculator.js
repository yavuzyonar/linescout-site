// OddsLighthouse odds calculator — pure client-side, no backend, no tracking of inputs.
(function () {
  function gcd(a, b) { return b === 0 ? a : gcd(b, a % b); }

  function toDecimal(value, format) {
    if (format === "decimal") {
      var d = parseFloat(value);
      return isFinite(d) && d > 1 ? d : null;
    }
    if (format === "american") {
      var a = parseFloat(value);
      if (!isFinite(a) || a === 0) return null;
      return a > 0 ? (a / 100) + 1 : (100 / Math.abs(a)) + 1;
    }
    if (format === "fractional") {
      var parts = String(value).split("/");
      if (parts.length !== 2) return null;
      var num = parseFloat(parts[0]), den = parseFloat(parts[1]);
      if (!isFinite(num) || !isFinite(den) || den === 0) return null;
      return (num / den) + 1;
    }
    return null;
  }

  function fromDecimalToAmerican(d) {
    if (d >= 2) return "+" + Math.round((d - 1) * 100);
    return "-" + Math.round(100 / (d - 1));
  }

  // Finds the simplest fraction (smallest denominator, up to maxDen) that's
  // within a small tolerance of `frac` — matches how sportsbooks quote
  // fractional odds (e.g. 0.6667 -> 2/3, not 6667/10000).
  function bestFraction(frac, maxDen) {
    var bestNum = Math.round(frac), bestDen = 1, bestErr = Math.abs(frac - Math.round(frac));
    for (var den = 1; den <= maxDen; den++) {
      var num = Math.round(frac * den);
      var err = Math.abs(frac - num / den);
      if (err < bestErr - 1e-9) {
        bestErr = err; bestNum = num; bestDen = den;
      }
      if (err < 1e-6) break;
    }
    var g = gcd(bestNum, bestDen) || 1;
    return [bestNum / g, bestDen / g];
  }

  function fromDecimalToFractional(d) {
    var frac = d - 1;
    var result = bestFraction(frac, 100);
    return result[0] + "/" + result[1];
  }

  function render() {
    var oddsInput = document.getElementById("calc-odds");
    var formatSelect = document.getElementById("calc-format");
    var stakeInput = document.getElementById("calc-stake");
    var results = document.getElementById("calc-results");
    if (!oddsInput || !formatSelect || !stakeInput || !results) return;

    var decimal = toDecimal(oddsInput.value, formatSelect.value);
    var stake = parseFloat(stakeInput.value);
    if (!isFinite(stake) || stake < 0) stake = 0;

    if (decimal === null) {
      results.innerHTML = '<p style="color:#94a0b2;">Enter valid odds to see the conversion.</p>';
      return;
    }

    var american = fromDecimalToAmerican(decimal);
    var fractional = fromDecimalToFractional(decimal);
    var impliedProb = (1 / decimal) * 100;
    var totalPayout = stake * decimal;
    var profit = totalPayout - stake;

    results.innerHTML =
      '<div class="result-row"><span>American odds</span><span>' + american + '</span></div>' +
      '<div class="result-row"><span>Decimal odds</span><span>' + decimal.toFixed(2) + '</span></div>' +
      '<div class="result-row"><span>Fractional odds</span><span>' + fractional + '</span></div>' +
      '<div class="result-row"><span>Implied probability</span><span>' + impliedProb.toFixed(1) + '%</span></div>' +
      '<div class="result-row"><span>Profit on $' + stake.toFixed(2) + ' stake</span><span>$' + profit.toFixed(2) + '</span></div>' +
      '<div class="result-row"><span>Total payout (stake + profit)</span><span>$' + totalPayout.toFixed(2) + '</span></div>';
  }

  document.addEventListener("DOMContentLoaded", function () {
    var oddsInput = document.getElementById("calc-odds");
    var formatSelect = document.getElementById("calc-format");
    var stakeInput = document.getElementById("calc-stake");
    if (!oddsInput) return;
    [oddsInput, formatSelect, stakeInput].forEach(function (el) {
      el.addEventListener("input", render);
      el.addEventListener("change", render);
    });
    render();
  });
})();

/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/css/models.css":
/*!****************************!*\
  !*** ./src/css/models.css ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ "./src/css/style.css":
/*!***************************!*\
  !*** ./src/css/style.css ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ "./src/js/index.js":
/*!*************************!*\
  !*** ./src/js/index.js ***!
  \*************************/
/***/ (() => {

// Models
var visualizer = new ModelVisualizer({container: "visualizer", editMode: false});;

var oldStepId = null;
var scale = d3.scaleLinear().range([0.3, 0.8]).domain([0, 5]).clamp(true);
var color = (d) => d3.interpolateYlGn(scale(d))

var count = {}
var failedStep = {}

function displayModels(models) {
  console.log("Update Graph...");

  visualizer.setModels(models);
  visualizer.repaint();
  repaintEdges();

  failedStep = {}
  count = {}
}

function setGraphLayoutOptions(options) {
  console.log(options);

  const graphDirectionsMap = {
    "Top-Bottom": "TB",
    "Bottom-Top": "BT",
    "Left-Right": "LR",
    "Right-Left": "RL"
  }

  const layoutOptions = {
    "rankdir": graphDirectionsMap[options["graphDirection"]],
    "nodesep": options["vertexSeparation"],
    "edgesep": options["edgeSeparation"],
    "ranksep": options["rankSeparation"]
  }

  visualizer.setGraphLayoutOptions(layoutOptions);
}

function repaintGraph() {
  visualizer.repaint();

  Object.keys(count).forEach(function (id) {
    drawStep(id, false);
  });

  if (failedStep.id) {
    updateFailedStep(failedStep);
  }
}

function repaintEdges() {
  // TODO: Remove the Model-Visualizer reset the color of the edge on repaint.

  Object.keys(count).forEach(function (id) {
    d3.select("svg g#" + id + " path")
      .style("stroke", "#7f8c8d");
  });
}

function updateStep(step) {
  var id = step["id"] || null;
  var visits = count[id] || 0;

  count[id] = visits + 1;

  if (oldStepId) {
    drawOldStep(oldStepId);
  }

  if (id) {
    drawStep(id, true);
  }

  oldStepId = id;
}

function drawStep(id, current) {
  d3.select("svg g#" + id + " rect")
    .style("fill", color(count[id]))
    .style("stroke", color(count[id]));

  d3.select("svg g#" + id + " path")
    .style("stroke", color(count[id]))

  if (current) {
    d3.select("svg g#" + id)
    .classed("current-node", true)
    .classed("current-edge", true);

    // Bold edges labels
    d3.selectAll("svg .edgeLabels tspan").attr("class", (d) => d.name == id ? "current-label" : "");
  }
}

function drawOldStep(id) {
  d3.select("svg g#" + id)
    .classed("current-node", false)
    .classed("current-edge", false);
}

function updateFailedStep(step) {
  failedStep = step;

  d3.select("svg g#" + step.id + " rect")
    .style("fill", "#c0392b")
    .style("stroke", "#c0392b");

  d3.select("svg g#" + step.id + " path")
    .style("stroke", "#c0392b")
}

// Resize

var dragging = false;

function dragstart(event) {
  event.preventDefault();
  dragging = true;
}

function dragmove(event) {
  if (dragging) {
    var percentage = (event.pageX / window.innerWidth) * 100;

    if (percentage > 30 && percentage < 70) {
      var rightPercentage = 100 - 0.05 - percentage;

      document.getElementById("left").style.width = percentage + "%";
      document.getElementById("right").style.width = rightPercentage + "%";
    }
  }
}

function dragend() {
  if (dragging) {
    repaintGraph();
  }

  dragging = false;
}

window.onload = function() {
  document.getElementById("dragbar").addEventListener("mousedown", function(e) { dragstart(e); });
  document.getElementById("dragbar").addEventListener("touchstart", function(e) { dragstart(e); });

  window.addEventListener("mousemove", function(e) { dragmove(e); });
  window.addEventListener("touchmove", function(e) { dragmove(e); });
  window.addEventListener("mouseup", dragend);
  window.addEventListener("touchend", dragend);
}

// Scripts

var port = null;
var ws = null;

var autoplay = false;
var maxDelay = 5;
var currentDelay = 5;

function percentageColor(percentage) {
  if (percentage < 50)
    return "badge-danger"

  if (percentage < 80)
    return "badge-warning"

  return "badge-success"
}

function showSetupOverlay() {
  document.getElementById("setup-overlay").classList.remove("d-none");
}

function hideSetupOverlay() {
  document.getElementById("setup-overlay").classList.add("d-none");

  hideErrorMessage();
  hideWarningMessage();
}

function showErrorMessage(message) {
  let errorAlert = document.getElementById("error-alert");
  errorAlert.classList.remove("d-none");
  errorAlert.classList.add("show");

  document.getElementById("error-message").textContent = message;
}

function hideErrorMessage() {
  document.getElementById("error-alert").classList.add("d-none");
}

function showWarningMessage(message) {
  let warningAlert = document.getElementById("warning-alert");
  warningAlert.classList.remove("d-none");
  warningAlert.classList.add("show");

  document.getElementById("warning-message").textContent = message;

  setTimeout(hideWarningMessage, 2000);
}

function hideWarningMessage() {
  document.getElementById("warning-alert").classList.add("d-none");
}

function showPortError() {
  document.getElementById("port-input").classList.add("is-invalid");
}

function showCurrentStepForm() {
  document.getElementById("current-step-form").classList.remove("d-none");
}

function hideCurrentStepForm() {
  document.getElementById("current-step-form").classList.add("d-none");
}

function showStatisticsForm() {
  document.getElementById("statistics-form").classList.remove("d-none");
}

function hideStatisticsForm() {
  document.getElementById("statistics-form").classList.add("d-none");
}

function showSettingsOverlay() {
  document.getElementById("settings-overlay").classList.remove("d-none");
}

function hideSettingsOverlay() {
  document.getElementById("settings-overlay").classList.add("d-none");
}

function showLoadingStartButton() {
  document.getElementById("start-button-loading").classList.remove("d-none");
  document.getElementById("start-button").classList.add("d-none");
}

function hideLoadingStartButton() {
  document.getElementById("start-button-loading").classList.add("d-none");
  document.getElementById("start-button").classList.remove("d-none");
}

function updateStepStart(step) {
  document.getElementById("id-input").value = step.id;
  document.getElementById("name-input").value = step.name;
  document.getElementById("model-input").value = step.modelName;

  if (step.data) {
    document.getElementById("data-input").value = JSON.stringify(step.data, null, '  ');
  }
}

function updateStepEnd(result) {
  let outputTextArea = document.getElementById("output-input");
  let autorscroll = document.getElementById("autoscroll-checkbox").checked;

  outputTextArea.value += result.output;

  if (autorscroll) {
    outputTextArea.scrollTop = outputTextArea.scrollHeight;
  }

  if (result.error) {
    updateFailedStep(result);

    document.getElementById("error-input").value = result.error.message;
    document.getElementById("trace-input").value = result.error.trace;
  }
}

function updateStatistics(statistics) {
  let status = document.getElementById("statistics-status")
  status.innerText = statistics.status ? "Passed" : "Failed";
  status.classList.add("badge")
  status.classList.add(statistics.status ? "badge-success" : "badge-danger");
  status.classList.remove(statistics.status ? "badge-danger" : "badge-success");


  document.getElementById("statistics-number-of-models").innerText = statistics.totalNumberOfModels;
  document.getElementById("statistics-completed-models").innerText = statistics.totalCompletedNumberOfModels;
  document.getElementById("statistics-failed-models").innerText = statistics.totalFailedNumberOfModels;
  document.getElementById("statistics-incomplete-models").innerText = statistics.totalIncompleteNumberOfModels;
  document.getElementById("statistics-not-executed-models").innerText = statistics.totalNotExecutedNumberOfModels;


  let edgeCoverage = document.getElementById("statistics-edge-coverage");
  edgeCoverage.innerText = statistics.edgeCoverage + "%";
  edgeCoverage.classList.remove(...["badge-danger", "badge-warning", "badge-success"]);
  edgeCoverage.classList.add(...["badge", percentageColor(statistics.edgeCoverage)]);

  document.getElementById("statistics-number-of-edges").innerText = statistics.totalNumberOfEdges;
  document.getElementById("statistics-visited-edges").innerText = statistics.totalNumberOfVisitedEdges;
  document.getElementById("statistics-unvisited-edges").innerText = statistics.totalNumberOfUnvisitedEdges;

  let vertexCoverage = document.getElementById("statistics-vertex-coverage");
  vertexCoverage.innerText = statistics.vertexCoverage + "%";
  vertexCoverage.classList.remove(...["badge-danger", "badge-warning", "badge-success"]);
  vertexCoverage.classList.add(...["badge", percentageColor(statistics.vertexCoverage)]);

  document.getElementById("statistics-number-of-vertices").innerText = statistics.totalNumberOfVertices;
  document.getElementById("statistics-visited-vertices").innerText = statistics.totalNumberOfVisitedVertices;
  document.getElementById("statistics-unvisited-vertices").innerText = statistics.totalNumberOfUnvisitedVertices;
}

function showAutoplayControls() {
  let controls = document.getElementById("autoplay-controls");
  controls.classList.add("d-inline-block");
  controls.classList.remove("d-none");
}

function hideAutoplayControls() {
  let controls = document.getElementById("autoplay-controls");
  controls.classList.remove("d-inline-block");
  controls.classList.add("d-none");
}

function showStopControls() {
  let controls = document.getElementById("stop-controls");
  controls.classList.add("d-inline-block");
  controls.classList.remove("d-none");
}

function hideStopControls() {
  let controls = document.getElementById("stop-controls");
  controls.classList.remove("d-inline-block");
  controls.classList.add("d-none");
}

function startCountDown(delay) {
  showAutoplayControls();
  document.getElementById("autoplay-seconds").innerText = currentDelay;

  if (currentDelay == 0) {
    ws.send(JSON.stringify({"autoplay": autoplay}));

    if (autoplay == false) {
      ws.close();
    }

    hideAutoplayControls();
    currentDelay = maxDelay;
  } else {
    setTimeout(function() {
      currentDelay = currentDelay > 0 ? currentDelay - 1 : 0;
      startCountDown();
    }, 1000);
  }
}

function skipCountDown() {
  currentDelay = 0;
}

function stopAutoplay() {
  autoplay = false;
  currentDelay = 0;
}

function stopRun() {
  hideStopControls();

  ws.send(JSON.stringify({"autoplay": autoplay}));
  ws.close();
}

function resetError() {
  document.getElementById("error-input").value = "";
  document.getElementById("trace-input").value = "";
}

function resetOutput() {
  document.getElementById("output-input").value = "";
}

function saveSettings() {
  const graphDirection = document.getElementById("graph-direction-input").value;
  const vertexSeparation = document.getElementById("vertex-separation-input").value;
  const edgeSeparation = document.getElementById("edge-separation-input").value;
  const rankSeparation = document.getElementById("rank-separation-input").value;

  setGraphLayoutOptions({
    "graphDirection": graphDirection,
    "vertexSeparation": vertexSeparation == 0 ? 50 : vertexSeparation,
    "edgeSeparation": edgeSeparation == 0 ? 50 : edgeSeparation,
    "rankSeparation": rankSeparation == 0 ? 50 : rankSeparation,
  });

  hideSettingsOverlay();
}

function connectToWebsocket() {
  console.log("Connect to websocket...");
  showLoadingStartButton();

  port = document.getElementById("port-input").value;
  autoplay = document.getElementById("autoplay-checkbox").checked;

  if (!port) {
    hideLoadingStartButton();
    showPortError();
    return
  }

  try {
    let open = false;
    let host = "localhost:" + port;
    ws = new WebSocket('ws://' + host + '/steps');

    console.log("Websocket Started.");

    ws.onerror = function(event) {
      console.log("Error", event);
      showSetupOverlay();
      showErrorMessage(`Could not connect to port: ${port}. Make sure the websocket server is running on the selected port.`);
    }
    ws.onopen = function(event) {
      ws.send(JSON.stringify({"autoplay": autoplay}));
      open = true;
    };
    ws.onclose = function(event) {
      hideLoadingStartButton();

      if (open) {
        showSetupOverlay();
        showWarningMessage(`Websocket connection closed.`);
      }
    }
    ws.onmessage = function(event) {
      var message = JSON.parse(event.data);

      if (message.models) {
        resetError();
        resetOutput();
        hideSetupOverlay();
        hideLoadingStartButton();

        showCurrentStepForm();
        hideStatisticsForm();

        displayModels(message.models);
      }

      if (message.step) {
        updateStep(message.step);
        updateStepStart(message.step);
      }

      if (message.result) {
        updateStepEnd(message.result);
      }

      if (message.statistics) {
        hideCurrentStepForm();
        showStatisticsForm();

        updateStatistics(message.statistics);
        if (autoplay) {
          startCountDown(maxDelay);
        } else {
          showStopControls();
        }
      }
    }
  } catch(error) {
    hideLoadingStartButton();
    showErrorMessage(`Unknown Error.`);
  }
}

window.addEventListener("resize", function(event) {
  repaintGraph()
});

window.onload = function() {
  document.getElementById("stop-button").addEventListener("click", function(event) {
    stopAutoplay();
  });
  document.getElementById("skip-button").addEventListener("click", function(event) {
    skipCountDown();
  });
  document.getElementById("stop-button").addEventListener("click", function(event) {
    stopRun();
  });

  document.getElementById("settings-button").addEventListener("click", function(event) {
    showSettingsOverlay();
  });
  document.getElementById("save-settings-button").addEventListener("click", function(event) {
    saveSettings();
  });
  document.getElementById("hide-settings-button").addEventListener("click", function(event) {
    hideSettingsOverlay();
  });

  document.getElementById("connect-button").addEventListener("click", function(event) {
    connectToWebsocket();
  });
}


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
/*!********************!*\
  !*** ./src/app.js ***!
  \********************/
__webpack_require__(/*! ./css/models.css */ "./src/css/models.css");
__webpack_require__(/*! ./css/style.css */ "./src/css/style.css");

__webpack_require__(/*! ./js/index.js */ "./src/js/index.js");

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/service-worker.js').then(registration => {
      console.log('SW registered: ', registration);
    }).catch(registrationError => {
      console.log('SW registration failed: ', registrationError);
    });
  });
}

})();

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoibWFpbi5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7OztBQUFBOzs7Ozs7Ozs7Ozs7O0FDQUE7Ozs7Ozs7Ozs7O0FDQUE7QUFDQSxzQ0FBc0MseUNBQXlDOztBQUUvRTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBO0FBQ0EsR0FBRzs7QUFFSDtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBLEdBQUc7QUFDSDs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7O0FBRUE7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0EsaUZBQWlGLGVBQWU7QUFDaEcsa0ZBQWtGLGVBQWU7O0FBRWpHLHFEQUFxRCxjQUFjO0FBQ25FLHFEQUFxRCxjQUFjO0FBQ25FO0FBQ0E7QUFDQTs7QUFFQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7O0FBR0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7O0FBR0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0EsNEJBQTRCLHFCQUFxQjs7QUFFakQ7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0EsS0FBSztBQUNMO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUEsMEJBQTBCLHFCQUFxQjtBQUMvQztBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxHQUFHOztBQUVIO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQSxxREFBcUQsS0FBSztBQUMxRDtBQUNBO0FBQ0EsOEJBQThCLHFCQUFxQjtBQUNuRDtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTtBQUNBLFVBQVU7QUFDVjtBQUNBO0FBQ0E7QUFDQTtBQUNBLElBQUk7QUFDSjtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0EsQ0FBQzs7QUFFRDtBQUNBO0FBQ0E7QUFDQSxHQUFHO0FBQ0g7QUFDQTtBQUNBLEdBQUc7QUFDSDtBQUNBO0FBQ0EsR0FBRzs7QUFFSDtBQUNBO0FBQ0EsR0FBRztBQUNIO0FBQ0E7QUFDQSxHQUFHO0FBQ0g7QUFDQTtBQUNBLEdBQUc7O0FBRUg7QUFDQTtBQUNBLEdBQUc7QUFDSDs7Ozs7OztVQ3ZmQTtVQUNBOztVQUVBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBO1VBQ0E7VUFDQTtVQUNBOztVQUVBO1VBQ0E7O1VBRUE7VUFDQTtVQUNBOzs7OztXQ3RCQTtXQUNBO1dBQ0E7V0FDQSx1REFBdUQsaUJBQWlCO1dBQ3hFO1dBQ0EsZ0RBQWdELGFBQWE7V0FDN0Q7Ozs7Ozs7Ozs7QUNOQSxtQkFBTyxDQUFDLDhDQUFrQjtBQUMxQixtQkFBTyxDQUFDLDRDQUFpQjs7QUFFekIsbUJBQU8sQ0FBQyx3Q0FBZTs7QUFFdkI7QUFDQTtBQUNBO0FBQ0E7QUFDQSxLQUFLO0FBQ0w7QUFDQSxLQUFLO0FBQ0wsR0FBRztBQUNIIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vYWx0d2Fsa2VyLWxpdmUtdmlld2VyLy4vc3JjL2Nzcy9tb2RlbHMuY3NzPzNlZTQiLCJ3ZWJwYWNrOi8vYWx0d2Fsa2VyLWxpdmUtdmlld2VyLy4vc3JjL2Nzcy9zdHlsZS5jc3M/NmI3YiIsIndlYnBhY2s6Ly9hbHR3YWxrZXItbGl2ZS12aWV3ZXIvLi9zcmMvanMvaW5kZXguanMiLCJ3ZWJwYWNrOi8vYWx0d2Fsa2VyLWxpdmUtdmlld2VyL3dlYnBhY2svYm9vdHN0cmFwIiwid2VicGFjazovL2FsdHdhbGtlci1saXZlLXZpZXdlci93ZWJwYWNrL3J1bnRpbWUvbWFrZSBuYW1lc3BhY2Ugb2JqZWN0Iiwid2VicGFjazovL2FsdHdhbGtlci1saXZlLXZpZXdlci8uL3NyYy9hcHAuanMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gZXh0cmFjdGVkIGJ5IG1pbmktY3NzLWV4dHJhY3QtcGx1Z2luXG5leHBvcnQge307IiwiLy8gZXh0cmFjdGVkIGJ5IG1pbmktY3NzLWV4dHJhY3QtcGx1Z2luXG5leHBvcnQge307IiwiLy8gTW9kZWxzXG52YXIgdmlzdWFsaXplciA9IG5ldyBNb2RlbFZpc3VhbGl6ZXIoe2NvbnRhaW5lcjogXCJ2aXN1YWxpemVyXCIsIGVkaXRNb2RlOiBmYWxzZX0pOztcblxudmFyIG9sZFN0ZXBJZCA9IG51bGw7XG52YXIgc2NhbGUgPSBkMy5zY2FsZUxpbmVhcigpLnJhbmdlKFswLjMsIDAuOF0pLmRvbWFpbihbMCwgNV0pLmNsYW1wKHRydWUpO1xudmFyIGNvbG9yID0gKGQpID0+IGQzLmludGVycG9sYXRlWWxHbihzY2FsZShkKSlcblxudmFyIGNvdW50ID0ge31cbnZhciBmYWlsZWRTdGVwID0ge31cblxuZnVuY3Rpb24gZGlzcGxheU1vZGVscyhtb2RlbHMpIHtcbiAgY29uc29sZS5sb2coXCJVcGRhdGUgR3JhcGguLi5cIik7XG5cbiAgdmlzdWFsaXplci5zZXRNb2RlbHMobW9kZWxzKTtcbiAgdmlzdWFsaXplci5yZXBhaW50KCk7XG4gIHJlcGFpbnRFZGdlcygpO1xuXG4gIGZhaWxlZFN0ZXAgPSB7fVxuICBjb3VudCA9IHt9XG59XG5cbmZ1bmN0aW9uIHNldEdyYXBoTGF5b3V0T3B0aW9ucyhvcHRpb25zKSB7XG4gIGNvbnNvbGUubG9nKG9wdGlvbnMpO1xuXG4gIGNvbnN0IGdyYXBoRGlyZWN0aW9uc01hcCA9IHtcbiAgICBcIlRvcC1Cb3R0b21cIjogXCJUQlwiLFxuICAgIFwiQm90dG9tLVRvcFwiOiBcIkJUXCIsXG4gICAgXCJMZWZ0LVJpZ2h0XCI6IFwiTFJcIixcbiAgICBcIlJpZ2h0LUxlZnRcIjogXCJSTFwiXG4gIH1cblxuICBjb25zdCBsYXlvdXRPcHRpb25zID0ge1xuICAgIFwicmFua2RpclwiOiBncmFwaERpcmVjdGlvbnNNYXBbb3B0aW9uc1tcImdyYXBoRGlyZWN0aW9uXCJdXSxcbiAgICBcIm5vZGVzZXBcIjogb3B0aW9uc1tcInZlcnRleFNlcGFyYXRpb25cIl0sXG4gICAgXCJlZGdlc2VwXCI6IG9wdGlvbnNbXCJlZGdlU2VwYXJhdGlvblwiXSxcbiAgICBcInJhbmtzZXBcIjogb3B0aW9uc1tcInJhbmtTZXBhcmF0aW9uXCJdXG4gIH1cblxuICB2aXN1YWxpemVyLnNldEdyYXBoTGF5b3V0T3B0aW9ucyhsYXlvdXRPcHRpb25zKTtcbn1cblxuZnVuY3Rpb24gcmVwYWludEdyYXBoKCkge1xuICB2aXN1YWxpemVyLnJlcGFpbnQoKTtcblxuICBPYmplY3Qua2V5cyhjb3VudCkuZm9yRWFjaChmdW5jdGlvbiAoaWQpIHtcbiAgICBkcmF3U3RlcChpZCwgZmFsc2UpO1xuICB9KTtcblxuICBpZiAoZmFpbGVkU3RlcC5pZCkge1xuICAgIHVwZGF0ZUZhaWxlZFN0ZXAoZmFpbGVkU3RlcCk7XG4gIH1cbn1cblxuZnVuY3Rpb24gcmVwYWludEVkZ2VzKCkge1xuICAvLyBUT0RPOiBSZW1vdmUgdGhlIE1vZGVsLVZpc3VhbGl6ZXIgcmVzZXQgdGhlIGNvbG9yIG9mIHRoZSBlZGdlIG9uIHJlcGFpbnQuXG5cbiAgT2JqZWN0LmtleXMoY291bnQpLmZvckVhY2goZnVuY3Rpb24gKGlkKSB7XG4gICAgZDMuc2VsZWN0KFwic3ZnIGcjXCIgKyBpZCArIFwiIHBhdGhcIilcbiAgICAgIC5zdHlsZShcInN0cm9rZVwiLCBcIiM3ZjhjOGRcIik7XG4gIH0pO1xufVxuXG5mdW5jdGlvbiB1cGRhdGVTdGVwKHN0ZXApIHtcbiAgdmFyIGlkID0gc3RlcFtcImlkXCJdIHx8IG51bGw7XG4gIHZhciB2aXNpdHMgPSBjb3VudFtpZF0gfHwgMDtcblxuICBjb3VudFtpZF0gPSB2aXNpdHMgKyAxO1xuXG4gIGlmIChvbGRTdGVwSWQpIHtcbiAgICBkcmF3T2xkU3RlcChvbGRTdGVwSWQpO1xuICB9XG5cbiAgaWYgKGlkKSB7XG4gICAgZHJhd1N0ZXAoaWQsIHRydWUpO1xuICB9XG5cbiAgb2xkU3RlcElkID0gaWQ7XG59XG5cbmZ1bmN0aW9uIGRyYXdTdGVwKGlkLCBjdXJyZW50KSB7XG4gIGQzLnNlbGVjdChcInN2ZyBnI1wiICsgaWQgKyBcIiByZWN0XCIpXG4gICAgLnN0eWxlKFwiZmlsbFwiLCBjb2xvcihjb3VudFtpZF0pKVxuICAgIC5zdHlsZShcInN0cm9rZVwiLCBjb2xvcihjb3VudFtpZF0pKTtcblxuICBkMy5zZWxlY3QoXCJzdmcgZyNcIiArIGlkICsgXCIgcGF0aFwiKVxuICAgIC5zdHlsZShcInN0cm9rZVwiLCBjb2xvcihjb3VudFtpZF0pKVxuXG4gIGlmIChjdXJyZW50KSB7XG4gICAgZDMuc2VsZWN0KFwic3ZnIGcjXCIgKyBpZClcbiAgICAuY2xhc3NlZChcImN1cnJlbnQtbm9kZVwiLCB0cnVlKVxuICAgIC5jbGFzc2VkKFwiY3VycmVudC1lZGdlXCIsIHRydWUpO1xuXG4gICAgLy8gQm9sZCBlZGdlcyBsYWJlbHNcbiAgICBkMy5zZWxlY3RBbGwoXCJzdmcgLmVkZ2VMYWJlbHMgdHNwYW5cIikuYXR0cihcImNsYXNzXCIsIChkKSA9PiBkLm5hbWUgPT0gaWQgPyBcImN1cnJlbnQtbGFiZWxcIiA6IFwiXCIpO1xuICB9XG59XG5cbmZ1bmN0aW9uIGRyYXdPbGRTdGVwKGlkKSB7XG4gIGQzLnNlbGVjdChcInN2ZyBnI1wiICsgaWQpXG4gICAgLmNsYXNzZWQoXCJjdXJyZW50LW5vZGVcIiwgZmFsc2UpXG4gICAgLmNsYXNzZWQoXCJjdXJyZW50LWVkZ2VcIiwgZmFsc2UpO1xufVxuXG5mdW5jdGlvbiB1cGRhdGVGYWlsZWRTdGVwKHN0ZXApIHtcbiAgZmFpbGVkU3RlcCA9IHN0ZXA7XG5cbiAgZDMuc2VsZWN0KFwic3ZnIGcjXCIgKyBzdGVwLmlkICsgXCIgcmVjdFwiKVxuICAgIC5zdHlsZShcImZpbGxcIiwgXCIjYzAzOTJiXCIpXG4gICAgLnN0eWxlKFwic3Ryb2tlXCIsIFwiI2MwMzkyYlwiKTtcblxuICBkMy5zZWxlY3QoXCJzdmcgZyNcIiArIHN0ZXAuaWQgKyBcIiBwYXRoXCIpXG4gICAgLnN0eWxlKFwic3Ryb2tlXCIsIFwiI2MwMzkyYlwiKVxufVxuXG4vLyBSZXNpemVcblxudmFyIGRyYWdnaW5nID0gZmFsc2U7XG5cbmZ1bmN0aW9uIGRyYWdzdGFydChldmVudCkge1xuICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICBkcmFnZ2luZyA9IHRydWU7XG59XG5cbmZ1bmN0aW9uIGRyYWdtb3ZlKGV2ZW50KSB7XG4gIGlmIChkcmFnZ2luZykge1xuICAgIHZhciBwZXJjZW50YWdlID0gKGV2ZW50LnBhZ2VYIC8gd2luZG93LmlubmVyV2lkdGgpICogMTAwO1xuXG4gICAgaWYgKHBlcmNlbnRhZ2UgPiAzMCAmJiBwZXJjZW50YWdlIDwgNzApIHtcbiAgICAgIHZhciByaWdodFBlcmNlbnRhZ2UgPSAxMDAgLSAwLjA1IC0gcGVyY2VudGFnZTtcblxuICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJsZWZ0XCIpLnN0eWxlLndpZHRoID0gcGVyY2VudGFnZSArIFwiJVwiO1xuICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJyaWdodFwiKS5zdHlsZS53aWR0aCA9IHJpZ2h0UGVyY2VudGFnZSArIFwiJVwiO1xuICAgIH1cbiAgfVxufVxuXG5mdW5jdGlvbiBkcmFnZW5kKCkge1xuICBpZiAoZHJhZ2dpbmcpIHtcbiAgICByZXBhaW50R3JhcGgoKTtcbiAgfVxuXG4gIGRyYWdnaW5nID0gZmFsc2U7XG59XG5cbndpbmRvdy5vbmxvYWQgPSBmdW5jdGlvbigpIHtcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJkcmFnYmFyXCIpLmFkZEV2ZW50TGlzdGVuZXIoXCJtb3VzZWRvd25cIiwgZnVuY3Rpb24oZSkgeyBkcmFnc3RhcnQoZSk7IH0pO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImRyYWdiYXJcIikuYWRkRXZlbnRMaXN0ZW5lcihcInRvdWNoc3RhcnRcIiwgZnVuY3Rpb24oZSkgeyBkcmFnc3RhcnQoZSk7IH0pO1xuXG4gIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwibW91c2Vtb3ZlXCIsIGZ1bmN0aW9uKGUpIHsgZHJhZ21vdmUoZSk7IH0pO1xuICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcihcInRvdWNobW92ZVwiLCBmdW5jdGlvbihlKSB7IGRyYWdtb3ZlKGUpOyB9KTtcbiAgd2luZG93LmFkZEV2ZW50TGlzdGVuZXIoXCJtb3VzZXVwXCIsIGRyYWdlbmQpO1xuICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcihcInRvdWNoZW5kXCIsIGRyYWdlbmQpO1xufVxuXG4vLyBTY3JpcHRzXG5cbnZhciBwb3J0ID0gbnVsbDtcbnZhciB3cyA9IG51bGw7XG5cbnZhciBhdXRvcGxheSA9IGZhbHNlO1xudmFyIG1heERlbGF5ID0gNTtcbnZhciBjdXJyZW50RGVsYXkgPSA1O1xuXG5mdW5jdGlvbiBwZXJjZW50YWdlQ29sb3IocGVyY2VudGFnZSkge1xuICBpZiAocGVyY2VudGFnZSA8IDUwKVxuICAgIHJldHVybiBcImJhZGdlLWRhbmdlclwiXG5cbiAgaWYgKHBlcmNlbnRhZ2UgPCA4MClcbiAgICByZXR1cm4gXCJiYWRnZS13YXJuaW5nXCJcblxuICByZXR1cm4gXCJiYWRnZS1zdWNjZXNzXCJcbn1cblxuZnVuY3Rpb24gc2hvd1NldHVwT3ZlcmxheSgpIHtcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzZXR1cC1vdmVybGF5XCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJkLW5vbmVcIik7XG59XG5cbmZ1bmN0aW9uIGhpZGVTZXR1cE92ZXJsYXkoKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic2V0dXAtb3ZlcmxheVwiKS5jbGFzc0xpc3QuYWRkKFwiZC1ub25lXCIpO1xuXG4gIGhpZGVFcnJvck1lc3NhZ2UoKTtcbiAgaGlkZVdhcm5pbmdNZXNzYWdlKCk7XG59XG5cbmZ1bmN0aW9uIHNob3dFcnJvck1lc3NhZ2UobWVzc2FnZSkge1xuICBsZXQgZXJyb3JBbGVydCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiZXJyb3ItYWxlcnRcIik7XG4gIGVycm9yQWxlcnQuY2xhc3NMaXN0LnJlbW92ZShcImQtbm9uZVwiKTtcbiAgZXJyb3JBbGVydC5jbGFzc0xpc3QuYWRkKFwic2hvd1wiKTtcblxuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImVycm9yLW1lc3NhZ2VcIikudGV4dENvbnRlbnQgPSBtZXNzYWdlO1xufVxuXG5mdW5jdGlvbiBoaWRlRXJyb3JNZXNzYWdlKCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImVycm9yLWFsZXJ0XCIpLmNsYXNzTGlzdC5hZGQoXCJkLW5vbmVcIik7XG59XG5cbmZ1bmN0aW9uIHNob3dXYXJuaW5nTWVzc2FnZShtZXNzYWdlKSB7XG4gIGxldCB3YXJuaW5nQWxlcnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIndhcm5pbmctYWxlcnRcIik7XG4gIHdhcm5pbmdBbGVydC5jbGFzc0xpc3QucmVtb3ZlKFwiZC1ub25lXCIpO1xuICB3YXJuaW5nQWxlcnQuY2xhc3NMaXN0LmFkZChcInNob3dcIik7XG5cbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJ3YXJuaW5nLW1lc3NhZ2VcIikudGV4dENvbnRlbnQgPSBtZXNzYWdlO1xuXG4gIHNldFRpbWVvdXQoaGlkZVdhcm5pbmdNZXNzYWdlLCAyMDAwKTtcbn1cblxuZnVuY3Rpb24gaGlkZVdhcm5pbmdNZXNzYWdlKCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIndhcm5pbmctYWxlcnRcIikuY2xhc3NMaXN0LmFkZChcImQtbm9uZVwiKTtcbn1cblxuZnVuY3Rpb24gc2hvd1BvcnRFcnJvcigpIHtcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJwb3J0LWlucHV0XCIpLmNsYXNzTGlzdC5hZGQoXCJpcy1pbnZhbGlkXCIpO1xufVxuXG5mdW5jdGlvbiBzaG93Q3VycmVudFN0ZXBGb3JtKCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImN1cnJlbnQtc3RlcC1mb3JtXCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJkLW5vbmVcIik7XG59XG5cbmZ1bmN0aW9uIGhpZGVDdXJyZW50U3RlcEZvcm0oKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiY3VycmVudC1zdGVwLWZvcm1cIikuY2xhc3NMaXN0LmFkZChcImQtbm9uZVwiKTtcbn1cblxuZnVuY3Rpb24gc2hvd1N0YXRpc3RpY3NGb3JtKCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXRpc3RpY3MtZm9ybVwiKS5jbGFzc0xpc3QucmVtb3ZlKFwiZC1ub25lXCIpO1xufVxuXG5mdW5jdGlvbiBoaWRlU3RhdGlzdGljc0Zvcm0oKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic3RhdGlzdGljcy1mb3JtXCIpLmNsYXNzTGlzdC5hZGQoXCJkLW5vbmVcIik7XG59XG5cbmZ1bmN0aW9uIHNob3dTZXR0aW5nc092ZXJsYXkoKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic2V0dGluZ3Mtb3ZlcmxheVwiKS5jbGFzc0xpc3QucmVtb3ZlKFwiZC1ub25lXCIpO1xufVxuXG5mdW5jdGlvbiBoaWRlU2V0dGluZ3NPdmVybGF5KCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInNldHRpbmdzLW92ZXJsYXlcIikuY2xhc3NMaXN0LmFkZChcImQtbm9uZVwiKTtcbn1cblxuZnVuY3Rpb24gc2hvd0xvYWRpbmdTdGFydEJ1dHRvbigpIHtcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGFydC1idXR0b24tbG9hZGluZ1wiKS5jbGFzc0xpc3QucmVtb3ZlKFwiZC1ub25lXCIpO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXJ0LWJ1dHRvblwiKS5jbGFzc0xpc3QuYWRkKFwiZC1ub25lXCIpO1xufVxuXG5mdW5jdGlvbiBoaWRlTG9hZGluZ1N0YXJ0QnV0dG9uKCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXJ0LWJ1dHRvbi1sb2FkaW5nXCIpLmNsYXNzTGlzdC5hZGQoXCJkLW5vbmVcIik7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic3RhcnQtYnV0dG9uXCIpLmNsYXNzTGlzdC5yZW1vdmUoXCJkLW5vbmVcIik7XG59XG5cbmZ1bmN0aW9uIHVwZGF0ZVN0ZXBTdGFydChzdGVwKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiaWQtaW5wdXRcIikudmFsdWUgPSBzdGVwLmlkO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIm5hbWUtaW5wdXRcIikudmFsdWUgPSBzdGVwLm5hbWU7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwibW9kZWwtaW5wdXRcIikudmFsdWUgPSBzdGVwLm1vZGVsTmFtZTtcblxuICBpZiAoc3RlcC5kYXRhKSB7XG4gICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJkYXRhLWlucHV0XCIpLnZhbHVlID0gSlNPTi5zdHJpbmdpZnkoc3RlcC5kYXRhLCBudWxsLCAnICAnKTtcbiAgfVxufVxuXG5mdW5jdGlvbiB1cGRhdGVTdGVwRW5kKHJlc3VsdCkge1xuICBsZXQgb3V0cHV0VGV4dEFyZWEgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIm91dHB1dC1pbnB1dFwiKTtcbiAgbGV0IGF1dG9yc2Nyb2xsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJhdXRvc2Nyb2xsLWNoZWNrYm94XCIpLmNoZWNrZWQ7XG5cbiAgb3V0cHV0VGV4dEFyZWEudmFsdWUgKz0gcmVzdWx0Lm91dHB1dDtcblxuICBpZiAoYXV0b3JzY3JvbGwpIHtcbiAgICBvdXRwdXRUZXh0QXJlYS5zY3JvbGxUb3AgPSBvdXRwdXRUZXh0QXJlYS5zY3JvbGxIZWlnaHQ7XG4gIH1cblxuICBpZiAocmVzdWx0LmVycm9yKSB7XG4gICAgdXBkYXRlRmFpbGVkU3RlcChyZXN1bHQpO1xuXG4gICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJlcnJvci1pbnB1dFwiKS52YWx1ZSA9IHJlc3VsdC5lcnJvci5tZXNzYWdlO1xuICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwidHJhY2UtaW5wdXRcIikudmFsdWUgPSByZXN1bHQuZXJyb3IudHJhY2U7XG4gIH1cbn1cblxuZnVuY3Rpb24gdXBkYXRlU3RhdGlzdGljcyhzdGF0aXN0aWNzKSB7XG4gIGxldCBzdGF0dXMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXRpc3RpY3Mtc3RhdHVzXCIpXG4gIHN0YXR1cy5pbm5lclRleHQgPSBzdGF0aXN0aWNzLnN0YXR1cyA/IFwiUGFzc2VkXCIgOiBcIkZhaWxlZFwiO1xuICBzdGF0dXMuY2xhc3NMaXN0LmFkZChcImJhZGdlXCIpXG4gIHN0YXR1cy5jbGFzc0xpc3QuYWRkKHN0YXRpc3RpY3Muc3RhdHVzID8gXCJiYWRnZS1zdWNjZXNzXCIgOiBcImJhZGdlLWRhbmdlclwiKTtcbiAgc3RhdHVzLmNsYXNzTGlzdC5yZW1vdmUoc3RhdGlzdGljcy5zdGF0dXMgPyBcImJhZGdlLWRhbmdlclwiIDogXCJiYWRnZS1zdWNjZXNzXCIpO1xuXG5cbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGF0aXN0aWNzLW51bWJlci1vZi1tb2RlbHNcIikuaW5uZXJUZXh0ID0gc3RhdGlzdGljcy50b3RhbE51bWJlck9mTW9kZWxzO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXRpc3RpY3MtY29tcGxldGVkLW1vZGVsc1wiKS5pbm5lclRleHQgPSBzdGF0aXN0aWNzLnRvdGFsQ29tcGxldGVkTnVtYmVyT2ZNb2RlbHM7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic3RhdGlzdGljcy1mYWlsZWQtbW9kZWxzXCIpLmlubmVyVGV4dCA9IHN0YXRpc3RpY3MudG90YWxGYWlsZWROdW1iZXJPZk1vZGVscztcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGF0aXN0aWNzLWluY29tcGxldGUtbW9kZWxzXCIpLmlubmVyVGV4dCA9IHN0YXRpc3RpY3MudG90YWxJbmNvbXBsZXRlTnVtYmVyT2ZNb2RlbHM7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic3RhdGlzdGljcy1ub3QtZXhlY3V0ZWQtbW9kZWxzXCIpLmlubmVyVGV4dCA9IHN0YXRpc3RpY3MudG90YWxOb3RFeGVjdXRlZE51bWJlck9mTW9kZWxzO1xuXG5cbiAgbGV0IGVkZ2VDb3ZlcmFnZSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic3RhdGlzdGljcy1lZGdlLWNvdmVyYWdlXCIpO1xuICBlZGdlQ292ZXJhZ2UuaW5uZXJUZXh0ID0gc3RhdGlzdGljcy5lZGdlQ292ZXJhZ2UgKyBcIiVcIjtcbiAgZWRnZUNvdmVyYWdlLmNsYXNzTGlzdC5yZW1vdmUoLi4uW1wiYmFkZ2UtZGFuZ2VyXCIsIFwiYmFkZ2Utd2FybmluZ1wiLCBcImJhZGdlLXN1Y2Nlc3NcIl0pO1xuICBlZGdlQ292ZXJhZ2UuY2xhc3NMaXN0LmFkZCguLi5bXCJiYWRnZVwiLCBwZXJjZW50YWdlQ29sb3Ioc3RhdGlzdGljcy5lZGdlQ292ZXJhZ2UpXSk7XG5cbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGF0aXN0aWNzLW51bWJlci1vZi1lZGdlc1wiKS5pbm5lclRleHQgPSBzdGF0aXN0aWNzLnRvdGFsTnVtYmVyT2ZFZGdlcztcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGF0aXN0aWNzLXZpc2l0ZWQtZWRnZXNcIikuaW5uZXJUZXh0ID0gc3RhdGlzdGljcy50b3RhbE51bWJlck9mVmlzaXRlZEVkZ2VzO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXRpc3RpY3MtdW52aXNpdGVkLWVkZ2VzXCIpLmlubmVyVGV4dCA9IHN0YXRpc3RpY3MudG90YWxOdW1iZXJPZlVudmlzaXRlZEVkZ2VzO1xuXG4gIGxldCB2ZXJ0ZXhDb3ZlcmFnZSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwic3RhdGlzdGljcy12ZXJ0ZXgtY292ZXJhZ2VcIik7XG4gIHZlcnRleENvdmVyYWdlLmlubmVyVGV4dCA9IHN0YXRpc3RpY3MudmVydGV4Q292ZXJhZ2UgKyBcIiVcIjtcbiAgdmVydGV4Q292ZXJhZ2UuY2xhc3NMaXN0LnJlbW92ZSguLi5bXCJiYWRnZS1kYW5nZXJcIiwgXCJiYWRnZS13YXJuaW5nXCIsIFwiYmFkZ2Utc3VjY2Vzc1wiXSk7XG4gIHZlcnRleENvdmVyYWdlLmNsYXNzTGlzdC5hZGQoLi4uW1wiYmFkZ2VcIiwgcGVyY2VudGFnZUNvbG9yKHN0YXRpc3RpY3MudmVydGV4Q292ZXJhZ2UpXSk7XG5cbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGF0aXN0aWNzLW51bWJlci1vZi12ZXJ0aWNlc1wiKS5pbm5lclRleHQgPSBzdGF0aXN0aWNzLnRvdGFsTnVtYmVyT2ZWZXJ0aWNlcztcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdGF0aXN0aWNzLXZpc2l0ZWQtdmVydGljZXNcIikuaW5uZXJUZXh0ID0gc3RhdGlzdGljcy50b3RhbE51bWJlck9mVmlzaXRlZFZlcnRpY2VzO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0YXRpc3RpY3MtdW52aXNpdGVkLXZlcnRpY2VzXCIpLmlubmVyVGV4dCA9IHN0YXRpc3RpY3MudG90YWxOdW1iZXJPZlVudmlzaXRlZFZlcnRpY2VzO1xufVxuXG5mdW5jdGlvbiBzaG93QXV0b3BsYXlDb250cm9scygpIHtcbiAgbGV0IGNvbnRyb2xzID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJhdXRvcGxheS1jb250cm9sc1wiKTtcbiAgY29udHJvbHMuY2xhc3NMaXN0LmFkZChcImQtaW5saW5lLWJsb2NrXCIpO1xuICBjb250cm9scy5jbGFzc0xpc3QucmVtb3ZlKFwiZC1ub25lXCIpO1xufVxuXG5mdW5jdGlvbiBoaWRlQXV0b3BsYXlDb250cm9scygpIHtcbiAgbGV0IGNvbnRyb2xzID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJhdXRvcGxheS1jb250cm9sc1wiKTtcbiAgY29udHJvbHMuY2xhc3NMaXN0LnJlbW92ZShcImQtaW5saW5lLWJsb2NrXCIpO1xuICBjb250cm9scy5jbGFzc0xpc3QuYWRkKFwiZC1ub25lXCIpO1xufVxuXG5mdW5jdGlvbiBzaG93U3RvcENvbnRyb2xzKCkge1xuICBsZXQgY29udHJvbHMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0b3AtY29udHJvbHNcIik7XG4gIGNvbnRyb2xzLmNsYXNzTGlzdC5hZGQoXCJkLWlubGluZS1ibG9ja1wiKTtcbiAgY29udHJvbHMuY2xhc3NMaXN0LnJlbW92ZShcImQtbm9uZVwiKTtcbn1cblxuZnVuY3Rpb24gaGlkZVN0b3BDb250cm9scygpIHtcbiAgbGV0IGNvbnRyb2xzID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzdG9wLWNvbnRyb2xzXCIpO1xuICBjb250cm9scy5jbGFzc0xpc3QucmVtb3ZlKFwiZC1pbmxpbmUtYmxvY2tcIik7XG4gIGNvbnRyb2xzLmNsYXNzTGlzdC5hZGQoXCJkLW5vbmVcIik7XG59XG5cbmZ1bmN0aW9uIHN0YXJ0Q291bnREb3duKGRlbGF5KSB7XG4gIHNob3dBdXRvcGxheUNvbnRyb2xzKCk7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiYXV0b3BsYXktc2Vjb25kc1wiKS5pbm5lclRleHQgPSBjdXJyZW50RGVsYXk7XG5cbiAgaWYgKGN1cnJlbnREZWxheSA9PSAwKSB7XG4gICAgd3Muc2VuZChKU09OLnN0cmluZ2lmeSh7XCJhdXRvcGxheVwiOiBhdXRvcGxheX0pKTtcblxuICAgIGlmIChhdXRvcGxheSA9PSBmYWxzZSkge1xuICAgICAgd3MuY2xvc2UoKTtcbiAgICB9XG5cbiAgICBoaWRlQXV0b3BsYXlDb250cm9scygpO1xuICAgIGN1cnJlbnREZWxheSA9IG1heERlbGF5O1xuICB9IGVsc2Uge1xuICAgIHNldFRpbWVvdXQoZnVuY3Rpb24oKSB7XG4gICAgICBjdXJyZW50RGVsYXkgPSBjdXJyZW50RGVsYXkgPiAwID8gY3VycmVudERlbGF5IC0gMSA6IDA7XG4gICAgICBzdGFydENvdW50RG93bigpO1xuICAgIH0sIDEwMDApO1xuICB9XG59XG5cbmZ1bmN0aW9uIHNraXBDb3VudERvd24oKSB7XG4gIGN1cnJlbnREZWxheSA9IDA7XG59XG5cbmZ1bmN0aW9uIHN0b3BBdXRvcGxheSgpIHtcbiAgYXV0b3BsYXkgPSBmYWxzZTtcbiAgY3VycmVudERlbGF5ID0gMDtcbn1cblxuZnVuY3Rpb24gc3RvcFJ1bigpIHtcbiAgaGlkZVN0b3BDb250cm9scygpO1xuXG4gIHdzLnNlbmQoSlNPTi5zdHJpbmdpZnkoe1wiYXV0b3BsYXlcIjogYXV0b3BsYXl9KSk7XG4gIHdzLmNsb3NlKCk7XG59XG5cbmZ1bmN0aW9uIHJlc2V0RXJyb3IoKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiZXJyb3ItaW5wdXRcIikudmFsdWUgPSBcIlwiO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInRyYWNlLWlucHV0XCIpLnZhbHVlID0gXCJcIjtcbn1cblxuZnVuY3Rpb24gcmVzZXRPdXRwdXQoKSB7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwib3V0cHV0LWlucHV0XCIpLnZhbHVlID0gXCJcIjtcbn1cblxuZnVuY3Rpb24gc2F2ZVNldHRpbmdzKCkge1xuICBjb25zdCBncmFwaERpcmVjdGlvbiA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiZ3JhcGgtZGlyZWN0aW9uLWlucHV0XCIpLnZhbHVlO1xuICBjb25zdCB2ZXJ0ZXhTZXBhcmF0aW9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJ2ZXJ0ZXgtc2VwYXJhdGlvbi1pbnB1dFwiKS52YWx1ZTtcbiAgY29uc3QgZWRnZVNlcGFyYXRpb24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImVkZ2Utc2VwYXJhdGlvbi1pbnB1dFwiKS52YWx1ZTtcbiAgY29uc3QgcmFua1NlcGFyYXRpb24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInJhbmstc2VwYXJhdGlvbi1pbnB1dFwiKS52YWx1ZTtcblxuICBzZXRHcmFwaExheW91dE9wdGlvbnMoe1xuICAgIFwiZ3JhcGhEaXJlY3Rpb25cIjogZ3JhcGhEaXJlY3Rpb24sXG4gICAgXCJ2ZXJ0ZXhTZXBhcmF0aW9uXCI6IHZlcnRleFNlcGFyYXRpb24gPT0gMCA/IDUwIDogdmVydGV4U2VwYXJhdGlvbixcbiAgICBcImVkZ2VTZXBhcmF0aW9uXCI6IGVkZ2VTZXBhcmF0aW9uID09IDAgPyA1MCA6IGVkZ2VTZXBhcmF0aW9uLFxuICAgIFwicmFua1NlcGFyYXRpb25cIjogcmFua1NlcGFyYXRpb24gPT0gMCA/IDUwIDogcmFua1NlcGFyYXRpb24sXG4gIH0pO1xuXG4gIGhpZGVTZXR0aW5nc092ZXJsYXkoKTtcbn1cblxuZnVuY3Rpb24gY29ubmVjdFRvV2Vic29ja2V0KCkge1xuICBjb25zb2xlLmxvZyhcIkNvbm5lY3QgdG8gd2Vic29ja2V0Li4uXCIpO1xuICBzaG93TG9hZGluZ1N0YXJ0QnV0dG9uKCk7XG5cbiAgcG9ydCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwicG9ydC1pbnB1dFwiKS52YWx1ZTtcbiAgYXV0b3BsYXkgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImF1dG9wbGF5LWNoZWNrYm94XCIpLmNoZWNrZWQ7XG5cbiAgaWYgKCFwb3J0KSB7XG4gICAgaGlkZUxvYWRpbmdTdGFydEJ1dHRvbigpO1xuICAgIHNob3dQb3J0RXJyb3IoKTtcbiAgICByZXR1cm5cbiAgfVxuXG4gIHRyeSB7XG4gICAgbGV0IG9wZW4gPSBmYWxzZTtcbiAgICBsZXQgaG9zdCA9IFwibG9jYWxob3N0OlwiICsgcG9ydDtcbiAgICB3cyA9IG5ldyBXZWJTb2NrZXQoJ3dzOi8vJyArIGhvc3QgKyAnL3N0ZXBzJyk7XG5cbiAgICBjb25zb2xlLmxvZyhcIldlYnNvY2tldCBTdGFydGVkLlwiKTtcblxuICAgIHdzLm9uZXJyb3IgPSBmdW5jdGlvbihldmVudCkge1xuICAgICAgY29uc29sZS5sb2coXCJFcnJvclwiLCBldmVudCk7XG4gICAgICBzaG93U2V0dXBPdmVybGF5KCk7XG4gICAgICBzaG93RXJyb3JNZXNzYWdlKGBDb3VsZCBub3QgY29ubmVjdCB0byBwb3J0OiAke3BvcnR9LiBNYWtlIHN1cmUgdGhlIHdlYnNvY2tldCBzZXJ2ZXIgaXMgcnVubmluZyBvbiB0aGUgc2VsZWN0ZWQgcG9ydC5gKTtcbiAgICB9XG4gICAgd3Mub25vcGVuID0gZnVuY3Rpb24oZXZlbnQpIHtcbiAgICAgIHdzLnNlbmQoSlNPTi5zdHJpbmdpZnkoe1wiYXV0b3BsYXlcIjogYXV0b3BsYXl9KSk7XG4gICAgICBvcGVuID0gdHJ1ZTtcbiAgICB9O1xuICAgIHdzLm9uY2xvc2UgPSBmdW5jdGlvbihldmVudCkge1xuICAgICAgaGlkZUxvYWRpbmdTdGFydEJ1dHRvbigpO1xuXG4gICAgICBpZiAob3Blbikge1xuICAgICAgICBzaG93U2V0dXBPdmVybGF5KCk7XG4gICAgICAgIHNob3dXYXJuaW5nTWVzc2FnZShgV2Vic29ja2V0IGNvbm5lY3Rpb24gY2xvc2VkLmApO1xuICAgICAgfVxuICAgIH1cbiAgICB3cy5vbm1lc3NhZ2UgPSBmdW5jdGlvbihldmVudCkge1xuICAgICAgdmFyIG1lc3NhZ2UgPSBKU09OLnBhcnNlKGV2ZW50LmRhdGEpO1xuXG4gICAgICBpZiAobWVzc2FnZS5tb2RlbHMpIHtcbiAgICAgICAgcmVzZXRFcnJvcigpO1xuICAgICAgICByZXNldE91dHB1dCgpO1xuICAgICAgICBoaWRlU2V0dXBPdmVybGF5KCk7XG4gICAgICAgIGhpZGVMb2FkaW5nU3RhcnRCdXR0b24oKTtcblxuICAgICAgICBzaG93Q3VycmVudFN0ZXBGb3JtKCk7XG4gICAgICAgIGhpZGVTdGF0aXN0aWNzRm9ybSgpO1xuXG4gICAgICAgIGRpc3BsYXlNb2RlbHMobWVzc2FnZS5tb2RlbHMpO1xuICAgICAgfVxuXG4gICAgICBpZiAobWVzc2FnZS5zdGVwKSB7XG4gICAgICAgIHVwZGF0ZVN0ZXAobWVzc2FnZS5zdGVwKTtcbiAgICAgICAgdXBkYXRlU3RlcFN0YXJ0KG1lc3NhZ2Uuc3RlcCk7XG4gICAgICB9XG5cbiAgICAgIGlmIChtZXNzYWdlLnJlc3VsdCkge1xuICAgICAgICB1cGRhdGVTdGVwRW5kKG1lc3NhZ2UucmVzdWx0KTtcbiAgICAgIH1cblxuICAgICAgaWYgKG1lc3NhZ2Uuc3RhdGlzdGljcykge1xuICAgICAgICBoaWRlQ3VycmVudFN0ZXBGb3JtKCk7XG4gICAgICAgIHNob3dTdGF0aXN0aWNzRm9ybSgpO1xuXG4gICAgICAgIHVwZGF0ZVN0YXRpc3RpY3MobWVzc2FnZS5zdGF0aXN0aWNzKTtcbiAgICAgICAgaWYgKGF1dG9wbGF5KSB7XG4gICAgICAgICAgc3RhcnRDb3VudERvd24obWF4RGVsYXkpO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIHNob3dTdG9wQ29udHJvbHMoKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgfSBjYXRjaChlcnJvcikge1xuICAgIGhpZGVMb2FkaW5nU3RhcnRCdXR0b24oKTtcbiAgICBzaG93RXJyb3JNZXNzYWdlKGBVbmtub3duIEVycm9yLmApO1xuICB9XG59XG5cbndpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwicmVzaXplXCIsIGZ1bmN0aW9uKGV2ZW50KSB7XG4gIHJlcGFpbnRHcmFwaCgpXG59KTtcblxud2luZG93Lm9ubG9hZCA9IGZ1bmN0aW9uKCkge1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0b3AtYnV0dG9uXCIpLmFkZEV2ZW50TGlzdGVuZXIoXCJjbGlja1wiLCBmdW5jdGlvbihldmVudCkge1xuICAgIHN0b3BBdXRvcGxheSgpO1xuICB9KTtcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJza2lwLWJ1dHRvblwiKS5hZGRFdmVudExpc3RlbmVyKFwiY2xpY2tcIiwgZnVuY3Rpb24oZXZlbnQpIHtcbiAgICBza2lwQ291bnREb3duKCk7XG4gIH0pO1xuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcInN0b3AtYnV0dG9uXCIpLmFkZEV2ZW50TGlzdGVuZXIoXCJjbGlja1wiLCBmdW5jdGlvbihldmVudCkge1xuICAgIHN0b3BSdW4oKTtcbiAgfSk7XG5cbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzZXR0aW5ncy1idXR0b25cIikuYWRkRXZlbnRMaXN0ZW5lcihcImNsaWNrXCIsIGZ1bmN0aW9uKGV2ZW50KSB7XG4gICAgc2hvd1NldHRpbmdzT3ZlcmxheSgpO1xuICB9KTtcbiAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJzYXZlLXNldHRpbmdzLWJ1dHRvblwiKS5hZGRFdmVudExpc3RlbmVyKFwiY2xpY2tcIiwgZnVuY3Rpb24oZXZlbnQpIHtcbiAgICBzYXZlU2V0dGluZ3MoKTtcbiAgfSk7XG4gIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiaGlkZS1zZXR0aW5ncy1idXR0b25cIikuYWRkRXZlbnRMaXN0ZW5lcihcImNsaWNrXCIsIGZ1bmN0aW9uKGV2ZW50KSB7XG4gICAgaGlkZVNldHRpbmdzT3ZlcmxheSgpO1xuICB9KTtcblxuICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImNvbm5lY3QtYnV0dG9uXCIpLmFkZEV2ZW50TGlzdGVuZXIoXCJjbGlja1wiLCBmdW5jdGlvbihldmVudCkge1xuICAgIGNvbm5lY3RUb1dlYnNvY2tldCgpO1xuICB9KTtcbn1cbiIsIi8vIFRoZSBtb2R1bGUgY2FjaGVcbnZhciBfX3dlYnBhY2tfbW9kdWxlX2NhY2hlX18gPSB7fTtcblxuLy8gVGhlIHJlcXVpcmUgZnVuY3Rpb25cbmZ1bmN0aW9uIF9fd2VicGFja19yZXF1aXJlX18obW9kdWxlSWQpIHtcblx0Ly8gQ2hlY2sgaWYgbW9kdWxlIGlzIGluIGNhY2hlXG5cdHZhciBjYWNoZWRNb2R1bGUgPSBfX3dlYnBhY2tfbW9kdWxlX2NhY2hlX19bbW9kdWxlSWRdO1xuXHRpZiAoY2FjaGVkTW9kdWxlICE9PSB1bmRlZmluZWQpIHtcblx0XHRyZXR1cm4gY2FjaGVkTW9kdWxlLmV4cG9ydHM7XG5cdH1cblx0Ly8gQ3JlYXRlIGEgbmV3IG1vZHVsZSAoYW5kIHB1dCBpdCBpbnRvIHRoZSBjYWNoZSlcblx0dmFyIG1vZHVsZSA9IF9fd2VicGFja19tb2R1bGVfY2FjaGVfX1ttb2R1bGVJZF0gPSB7XG5cdFx0Ly8gbm8gbW9kdWxlLmlkIG5lZWRlZFxuXHRcdC8vIG5vIG1vZHVsZS5sb2FkZWQgbmVlZGVkXG5cdFx0ZXhwb3J0czoge31cblx0fTtcblxuXHQvLyBFeGVjdXRlIHRoZSBtb2R1bGUgZnVuY3Rpb25cblx0X193ZWJwYWNrX21vZHVsZXNfX1ttb2R1bGVJZF0obW9kdWxlLCBtb2R1bGUuZXhwb3J0cywgX193ZWJwYWNrX3JlcXVpcmVfXyk7XG5cblx0Ly8gUmV0dXJuIHRoZSBleHBvcnRzIG9mIHRoZSBtb2R1bGVcblx0cmV0dXJuIG1vZHVsZS5leHBvcnRzO1xufVxuXG4iLCIvLyBkZWZpbmUgX19lc01vZHVsZSBvbiBleHBvcnRzXG5fX3dlYnBhY2tfcmVxdWlyZV9fLnIgPSAoZXhwb3J0cykgPT4ge1xuXHRpZih0eXBlb2YgU3ltYm9sICE9PSAndW5kZWZpbmVkJyAmJiBTeW1ib2wudG9TdHJpbmdUYWcpIHtcblx0XHRPYmplY3QuZGVmaW5lUHJvcGVydHkoZXhwb3J0cywgU3ltYm9sLnRvU3RyaW5nVGFnLCB7IHZhbHVlOiAnTW9kdWxlJyB9KTtcblx0fVxuXHRPYmplY3QuZGVmaW5lUHJvcGVydHkoZXhwb3J0cywgJ19fZXNNb2R1bGUnLCB7IHZhbHVlOiB0cnVlIH0pO1xufTsiLCJyZXF1aXJlKCcuL2Nzcy9tb2RlbHMuY3NzJyk7XG5yZXF1aXJlKCcuL2Nzcy9zdHlsZS5jc3MnKTtcblxucmVxdWlyZSgnLi9qcy9pbmRleC5qcycpO1xuXG5pZiAoJ3NlcnZpY2VXb3JrZXInIGluIG5hdmlnYXRvcikge1xuICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcignbG9hZCcsICgpID0+IHtcbiAgICBuYXZpZ2F0b3Iuc2VydmljZVdvcmtlci5yZWdpc3RlcignL3NlcnZpY2Utd29ya2VyLmpzJykudGhlbihyZWdpc3RyYXRpb24gPT4ge1xuICAgICAgY29uc29sZS5sb2coJ1NXIHJlZ2lzdGVyZWQ6ICcsIHJlZ2lzdHJhdGlvbik7XG4gICAgfSkuY2F0Y2gocmVnaXN0cmF0aW9uRXJyb3IgPT4ge1xuICAgICAgY29uc29sZS5sb2coJ1NXIHJlZ2lzdHJhdGlvbiBmYWlsZWQ6ICcsIHJlZ2lzdHJhdGlvbkVycm9yKTtcbiAgICB9KTtcbiAgfSk7XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=
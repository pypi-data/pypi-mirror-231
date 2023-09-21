/**
 * Copyright 2018 Google Inc. All Rights Reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// If the loader is already loaded, just stop.
if (!self.define) {
  let registry = {};

  // Used for `eval` and `importScripts` where we can't get script URL by other means.
  // In both cases, it's safe to use a global var because those functions are synchronous.
  let nextDefineUri;

  const singleRequire = (uri, parentUri) => {
    uri = new URL(uri + ".js", parentUri).href;
    return registry[uri] || (
      
        new Promise(resolve => {
          if ("document" in self) {
            const script = document.createElement("script");
            script.src = uri;
            script.onload = resolve;
            document.head.appendChild(script);
          } else {
            nextDefineUri = uri;
            importScripts(uri);
            resolve();
          }
        })
      
      .then(() => {
        let promise = registry[uri];
        if (!promise) {
          throw new Error(`Module ${uri} didn’t register its module`);
        }
        return promise;
      })
    );
  };

  self.define = (depsNames, factory) => {
    const uri = nextDefineUri || ("document" in self ? document.currentScript.src : "") || location.href;
    if (registry[uri]) {
      // Module is already loading or loaded.
      return;
    }
    let exports = {};
    const require = depUri => singleRequire(depUri, uri);
    const specialDeps = {
      module: { uri },
      exports,
      require
    };
    registry[uri] = Promise.all(depsNames.map(
      depName => specialDeps[depName] || require(depName)
    )).then(deps => {
      factory(...deps);
      return exports;
    });
  };
}
define(['./workbox-f49bc449'], (function (workbox) { 'use strict';

  self.skipWaiting();
  workbox.clientsClaim();

  /**
   * The precacheAndRoute() method efficiently caches and responds to
   * requests for URLs in the manifest.
   * See https://goo.gl/S9QRab
   */
  workbox.precacheAndRoute([{
    "url": "15c8420b0e6e542a978f.svg",
    "revision": null
  }, {
    "url": "68659bacae74b54ea28c.svg",
    "revision": null
  }, {
    "url": "c60ee78200e01104d302.svg",
    "revision": null
  }, {
    "url": "eb64b001bca05f6e3811.png",
    "revision": null
  }, {
    "url": "ec7bf1eb98b0b823dd6d.png",
    "revision": null
  }, {
    "url": "favicon.ico",
    "revision": "70944456df4773bb6161b98a71878da9"
  }, {
    "url": "feee962cf6af8043e5c8.svg",
    "revision": null
  }, {
    "url": "index.html",
    "revision": "8fea66ce9e3a5ab9534f0e5cc9aaa0ce"
  }, {
    "url": "main.css",
    "revision": "1514c964eb9034baa7479f17cbfaac81"
  }, {
    "url": "main.js",
    "revision": "9e1724cdf69fb0911b87fe918509586b"
  }], {});

}));
//# sourceMappingURL=service-worker.js.map

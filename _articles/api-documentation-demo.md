---
layout: api-demo
title: "Weather API Documentation - Interactive Demo"
description: "A comprehensive API documentation example demonstrating navigation, multiple endpoints, multi-language code samples, and developer-friendly design patterns."
date: 2023-01-01
tags: [Reference]
secondary_tags: [API Documentation, Developer Experience, Design]
---

{::nomarkdown}
<div class="api-demo-intro">
  <h1>Weather API Documentation</h1>
  <p>This interactive example demonstrates comprehensive API documentation design with navigation, multiple endpoints, multi-language code samples, and developer-friendly features.</p>
</div>

<div class="api-demo-wrapper">
  <div class="api-demo-container">
    <!-- Navigation Sidebar -->
    <div class="api-demo-nav">
      <div class="api-nav-section">
        <h3>Getting Started</h3>
        <div class="api-nav-item active" onclick="showEndpoint('auth', event)">Authentication</div>
        <div class="api-nav-item" onclick="showEndpoint('errors', event)">Error Codes</div>
      </div>
      <div class="api-nav-section">
        <h3>Endpoints</h3>
        <div class="api-nav-item" onclick="showEndpoint('current', event)">
          <span class="method-badge method-get">GET</span>Current Weather
        </div>
        <div class="api-nav-item" onclick="showEndpoint('forecast', event)">
          <span class="method-badge method-get">GET</span>7-Day Forecast
        </div>
        <div class="api-nav-item" onclick="showEndpoint('alerts', event)">
          <span class="method-badge method-post">POST</span>Weather Alerts
        </div>
      </div>
    </div>

    <!-- Content Area -->
    <div class="api-demo-content">
      <!-- Left Column: Documentation -->
      <div class="api-demo-left">

        <!-- Authentication Section -->
        <div id="auth" class="api-endpoint-section active">
          <h2>Authentication</h2>
          <p>All API requests require authentication using an API key. Include your API key in the request header or as a query parameter.</p>

          <h3>Header Authentication (Recommended)</h3>
          <div class="api-method-url">
            <code>Authorization: Bearer YOUR_API_KEY</code>
          </div>

          <h3>Query Parameter Authentication</h3>
          <div class="api-method-url">
            <code>?api_key=YOUR_API_KEY</code>
          </div>

          <div class="api-info-box">
            <strong>Rate Limits:</strong> 100 requests per hour for free tier. Premium accounts: 1000 requests per hour. Rate limit information is included in response headers.
          </div>

          <h3>Rate Limit Headers</h3>
          <table class="api-param-table">
            <tr>
              <th>Header</th>
              <th>Description</th>
            </tr>
            <tr>
              <td><code>X-RateLimit-Limit</code></td>
              <td>Maximum requests allowed per hour</td>
            </tr>
            <tr>
              <td><code>X-RateLimit-Remaining</code></td>
              <td>Requests remaining in current window</td>
            </tr>
            <tr>
              <td><code>X-RateLimit-Reset</code></td>
              <td>Time when rate limit resets (Unix timestamp)</td>
            </tr>
          </table>
        </div>

        <!-- Error Codes Section -->
        <div id="errors" class="api-endpoint-section">
          <h2>Error Codes</h2>
          <p>The API uses standard HTTP status codes to indicate success or failure.</p>

          <table class="api-status-table">
            <tr>
              <th>Status Code</th>
              <th>Description</th>
            </tr>
            <tr>
              <td><span class="api-status-code status-200">200 OK</span></td>
              <td>Request succeeded</td>
            </tr>
            <tr>
              <td><span class="api-status-code status-400">400 Bad Request</span></td>
              <td>Invalid parameters or malformed request</td>
            </tr>
            <tr>
              <td><span class="api-status-code status-401">401 Unauthorized</span></td>
              <td>Missing or invalid API key</td>
            </tr>
            <tr>
              <td><span class="api-status-code status-404">404 Not Found</span></td>
              <td>Location not found</td>
            </tr>
            <tr>
              <td><span class="api-status-code status-429">429 Too Many Requests</span></td>
              <td>Rate limit exceeded</td>
            </tr>
            <tr>
              <td><span class="api-status-code status-500">500 Internal Server Error</span></td>
              <td>Server error occurred</td>
            </tr>
          </table>

          <h3>Error Response Format</h3>
          <p>All error responses follow a consistent format:</p>
          <pre style="background:var(--color-bg);padding:1rem;border-radius:4px;color:var(--color-text);border:1px solid var(--color-border);"><code>{
  "error": true,
  "status": 400,
  "message": "Invalid location parameter",
  "code": "INVALID_LOCATION"
}</code></pre>
        </div>

        <!-- Current Weather Endpoint -->
        <div id="current" class="api-endpoint-section">
          <h2>Get Current Weather</h2>
          <p>Retrieve current weather information for a specified location including temperature, humidity, wind speed, and conditions.</p>

          <div class="api-method-url">
            <span class="method get">GET</span>
            <code>https://api.weather.example/v1/current</code>
          </div>

          <h3>Request Parameters</h3>
          <table class="api-param-table">
            <tr>
              <th>Parameter</th>
              <th>Type</th>
              <th>Required</th>
              <th>Description</th>
            </tr>
            <tr>
              <td><code>location</code></td>
              <td>string</td>
              <td><span class="api-required">Required</span></td>
              <td>City name or coordinates (lat,lon)</td>
            </tr>
            <tr>
              <td><code>units</code></td>
              <td>string</td>
              <td>Optional</td>
              <td>Temperature units: <code>metric</code> or <code>imperial</code>. Default: <code>metric</code></td>
            </tr>
            <tr>
              <td><code>lang</code></td>
              <td>string</td>
              <td>Optional</td>
              <td>Language code for weather descriptions. Default: <code>en</code></td>
            </tr>
          </table>

          <h3>Response Fields</h3>
          <table class="api-param-table">
            <tr>
              <th>Field</th>
              <th>Type</th>
              <th>Description</th>
            </tr>
            <tr>
              <td><code>location</code></td>
              <td>string</td>
              <td>Full location name</td>
            </tr>
            <tr>
              <td><code>temperature</code></td>
              <td>string</td>
              <td>Current temperature with unit</td>
            </tr>
            <tr>
              <td><code>feels_like</code></td>
              <td>string</td>
              <td>Perceived temperature</td>
            </tr>
            <tr>
              <td><code>humidity</code></td>
              <td>string</td>
              <td>Humidity percentage</td>
            </tr>
            <tr>
              <td><code>wind</code></td>
              <td>string</td>
              <td>Wind speed with unit</td>
            </tr>
            <tr>
              <td><code>description</code></td>
              <td>string</td>
              <td>Weather condition description</td>
            </tr>
            <tr>
              <td><code>timestamp</code></td>
              <td>integer</td>
              <td>Unix timestamp of observation</td>
            </tr>
          </table>
        </div>

        <!-- Forecast Endpoint -->
        <div id="forecast" class="api-endpoint-section">
          <h2>Get 7-Day Forecast</h2>
          <p>Retrieve a 7-day weather forecast with daily high/low temperatures and conditions.</p>

          <div class="api-method-url">
            <span class="method get">GET</span>
            <code>https://api.weather.example/v1/forecast</code>
          </div>

          <h3>Request Parameters</h3>
          <table class="api-param-table">
            <tr>
              <th>Parameter</th>
              <th>Type</th>
              <th>Required</th>
              <th>Description</th>
            </tr>
            <tr>
              <td><code>location</code></td>
              <td>string</td>
              <td><span class="api-required">Required</span></td>
              <td>City name or coordinates (lat,lon)</td>
            </tr>
            <tr>
              <td><code>days</code></td>
              <td>integer</td>
              <td>Optional</td>
              <td>Number of days (1-7). Default: <code>7</code></td>
            </tr>
            <tr>
              <td><code>units</code></td>
              <td>string</td>
              <td>Optional</td>
              <td>Temperature units: <code>metric</code> or <code>imperial</code></td>
            </tr>
          </table>

          <h3>Response Structure</h3>
          <p>Returns an array of daily forecast objects with high/low temperatures and weather descriptions.</p>
        </div>

        <!-- Alerts Endpoint -->
        <div id="alerts" class="api-endpoint-section">
          <h2>Subscribe to Weather Alerts</h2>
          <p>Subscribe to receive weather alerts for a specific location via webhook.</p>

          <div class="api-method-url">
            <span class="method post">POST</span>
            <code>https://api.weather.example/v1/alerts/subscribe</code>
          </div>

          <h3>Request Body</h3>
          <table class="api-param-table">
            <tr>
              <th>Field</th>
              <th>Type</th>
              <th>Required</th>
              <th>Description</th>
            </tr>
            <tr>
              <td><code>location</code></td>
              <td>string</td>
              <td><span class="api-required">Required</span></td>
              <td>City name or coordinates</td>
            </tr>
            <tr>
              <td><code>webhook_url</code></td>
              <td>string</td>
              <td><span class="api-required">Required</span></td>
              <td>URL to receive alert notifications</td>
            </tr>
            <tr>
              <td><code>alert_types</code></td>
              <td>array</td>
              <td><span class="api-required">Required</span></td>
              <td>Alert types: <code>storm</code>, <code>flood</code>, <code>heat</code>, <code>cold</code></td>
            </tr>
          </table>

          <h3>Response</h3>
          <p>Returns a subscription ID and confirmation of the active subscription.</p>
        </div>

      </div>

      <!-- Right Column: Code Examples -->
      <div class="api-demo-right">

        <!-- Auth Examples -->
        <div id="auth-examples" class="api-endpoint-section active">
          <div class="api-code-block">
            <div class="api-code-header">
              <div class="api-code-tabs">
                <button class="api-code-tab active" onclick="showCode('auth', 'curl', event)">cURL</button>
                <button class="api-code-tab" onclick="showCode('auth', 'python', event)">Python</button>
                <button class="api-code-tab" onclick="showCode('auth', 'javascript', event)">JavaScript</button>
              </div>
              <button class="api-copy-btn" onclick="copyCode('auth', event)">Copy</button>
            </div>
            <div class="api-code-content" id="auth-code-content">
              <div class="api-code-example active" id="auth-curl">
<pre><span class="comment"># Header authentication</span>
curl -X GET "https://api.weather.example/v1/current?location=NewYork" \
  -H "Authorization: Bearer YOUR_API_KEY"

<span class="comment"># Query parameter authentication</span>
curl -X GET "https://api.weather.example/v1/current?location=NewYork&api_key=YOUR_API_KEY"</pre>
              </div>
              <div class="api-code-example" id="auth-python">
<pre><span class="comment"># Header authentication</span>
import requests

headers = {
    <span class="key">"Authorization"</span>: <span class="string">"Bearer YOUR_API_KEY"</span>
}

response = requests.get(
    <span class="string">"https://api.weather.example/v1/current"</span>,
    params={<span class="key">"location"</span>: <span class="string">"New York"</span>},
    headers=headers
)

data = response.json()</pre>
              </div>
              <div class="api-code-example" id="auth-javascript">
<pre><span class="comment">// Header authentication</span>
fetch(<span class="string">'https://api.weather.example/v1/current?location=NewYork'</span>, {
  method: <span class="string">'GET'</span>,
  headers: {
    <span class="key">'Authorization'</span>: <span class="string">'Bearer YOUR_API_KEY'</span>
  }
})
  .then(response => response.json())
  .then(data => console.log(data));</pre>
              </div>
            </div>
          </div>
        </div>

        <!-- Error Examples -->
        <div id="errors-examples" class="api-endpoint-section">
          <h4 style="color:#e8d5d1;margin-top:0;font-size:0.9rem;">Example Error Responses</h4>
          <div class="api-code-block">
            <div class="api-code-header">
              <span style="color:#a89284;font-size:0.8rem;">401 Unauthorized</span>
            </div>
            <div class="api-code-content">
<pre>{
  <span class="key">"error"</span>: <span class="boolean">true</span>,
  <span class="key">"status"</span>: <span class="number">401</span>,
  <span class="key">"message"</span>: <span class="string">"Invalid API key"</span>,
  <span class="key">"code"</span>: <span class="string">"INVALID_API_KEY"</span>
}</pre>
            </div>
          </div>

          <div class="api-code-block">
            <div class="api-code-header">
              <span style="color:#a89284;font-size:0.8rem;">429 Rate Limit Exceeded</span>
            </div>
            <div class="api-code-content">
<pre>{
  <span class="key">"error"</span>: <span class="boolean">true</span>,
  <span class="key">"status"</span>: <span class="number">429</span>,
  <span class="key">"message"</span>: <span class="string">"Rate limit exceeded"</span>,
  <span class="key">"code"</span>: <span class="string">"RATE_LIMIT_EXCEEDED"</span>,
  <span class="key">"retry_after"</span>: <span class="number">3600</span>
}</pre>
            </div>
          </div>
        </div>

        <!-- Current Weather Examples -->
        <div id="current-examples" class="api-endpoint-section">
          <div class="api-code-block">
            <div class="api-code-header">
              <div class="api-code-tabs">
                <button class="api-code-tab active" onclick="showCode('current', 'curl', event)">cURL</button>
                <button class="api-code-tab" onclick="showCode('current', 'python', event)">Python</button>
                <button class="api-code-tab" onclick="showCode('current', 'javascript', event)">JavaScript</button>
              </div>
              <button class="api-copy-btn" onclick="copyCode('current', event)">Copy</button>
            </div>
            <div class="api-code-content" id="current-code-content">
              <div class="api-code-example active" id="current-curl">
<pre>curl -X GET "https://api.weather.example/v1/current?location=NewYork&units=metric" \
  -H "Authorization: Bearer YOUR_API_KEY"</pre>
              </div>
              <div class="api-code-example" id="current-python">
<pre>import requests

headers = {<span class="key">"Authorization"</span>: <span class="string">"Bearer YOUR_API_KEY"</span>}
params = {
    <span class="key">"location"</span>: <span class="string">"New York"</span>,
    <span class="key">"units"</span>: <span class="string">"metric"</span>
}

response = requests.get(
    <span class="string">"https://api.weather.example/v1/current"</span>,
    params=params,
    headers=headers
)

weather = response.json()
print(f<span class="string">"Temperature: {weather['temperature']}"</span>)</pre>
              </div>
              <div class="api-code-example" id="current-javascript">
<pre>const params = new URLSearchParams({
  location: <span class="string">'New York'</span>,
  units: <span class="string">'metric'</span>
});

fetch(<span class="string">`https://api.weather.example/v1/current?${params}`</span>, {
  headers: {
    <span class="key">'Authorization'</span>: <span class="string">'Bearer YOUR_API_KEY'</span>
  }
})
  .then(res => res.json())
  .then(data => {
    console.log(<span class="string">`Temperature: ${data.temperature}`</span>);
  });</pre>
              </div>
            </div>
          </div>

          <h4 style="color:#e8d5d1;margin-top:2rem;font-size:0.9rem;">Response (200 OK)</h4>
          <div class="api-code-block">
            <div class="api-code-content">
<pre>{
  <span class="key">"location"</span>: <span class="string">"New York, NY"</span>,
  <span class="key">"temperature"</span>: <span class="string">"15°C"</span>,
  <span class="key">"feels_like"</span>: <span class="string">"13°C"</span>,
  <span class="key">"humidity"</span>: <span class="string">"50%"</span>,
  <span class="key">"wind"</span>: <span class="string">"5 m/s"</span>,
  <span class="key">"description"</span>: <span class="string">"Partly cloudy"</span>,
  <span class="key">"timestamp"</span>: <span class="number">1699564800</span>
}</pre>
            </div>
          </div>
        </div>

        <!-- Forecast Examples -->
        <div id="forecast-examples" class="api-endpoint-section">
          <div class="api-code-block">
            <div class="api-code-header">
              <div class="api-code-tabs">
                <button class="api-code-tab active" onclick="showCode('forecast', 'curl', event)">cURL</button>
                <button class="api-code-tab" onclick="showCode('forecast', 'python', event)">Python</button>
                <button class="api-code-tab" onclick="showCode('forecast', 'javascript', event)">JavaScript</button>
              </div>
              <button class="api-copy-btn" onclick="copyCode('forecast', event)">Copy</button>
            </div>
            <div class="api-code-content" id="forecast-code-content">
              <div class="api-code-example active" id="forecast-curl">
<pre>curl -X GET "https://api.weather.example/v1/forecast?location=NewYork&days=7" \
  -H "Authorization: Bearer YOUR_API_KEY"</pre>
              </div>
              <div class="api-code-example" id="forecast-python">
<pre>import requests

response = requests.get(
    <span class="string">"https://api.weather.example/v1/forecast"</span>,
    params={<span class="key">"location"</span>: <span class="string">"New York"</span>, <span class="key">"days"</span>: <span class="number">7</span>},
    headers={<span class="key">"Authorization"</span>: <span class="string">"Bearer YOUR_API_KEY"</span>}
)

forecast = response.json()
for day in forecast[<span class="string">"days"</span>]:
    print(f<span class="string">"{day['date']}: {day['high']} / {day['low']}"</span>)</pre>
              </div>
              <div class="api-code-example" id="forecast-javascript">
<pre>fetch(<span class="string">'https://api.weather.example/v1/forecast?location=NewYork&days=7'</span>, {
  headers: {<span class="key">'Authorization'</span>: <span class="string">'Bearer YOUR_API_KEY'</span>}
})
  .then(res => res.json())
  .then(data => {
    data.days.forEach(day => {
      console.log(<span class="string">`${day.date}: ${day.high} / ${day.low}`</span>);
    });
  });</pre>
              </div>
            </div>
          </div>

          <h4 style="color:#e8d5d1;margin-top:2rem;font-size:0.9rem;">Response (200 OK)</h4>
          <div class="api-code-block">
            <div class="api-code-content">
<pre>{
  <span class="key">"location"</span>: <span class="string">"New York, NY"</span>,
  <span class="key">"days"</span>: [
    {
      <span class="key">"date"</span>: <span class="string">"2024-11-10"</span>,
      <span class="key">"high"</span>: <span class="string">"18°C"</span>,
      <span class="key">"low"</span>: <span class="string">"12°C"</span>,
      <span class="key">"description"</span>: <span class="string">"Sunny"</span>
    },
    <span class="comment">// ...</span>
  ]
}</pre>
            </div>
          </div>
        </div>

        <!-- Alerts Examples -->
        <div id="alerts-examples" class="api-endpoint-section">
          <div class="api-code-block">
            <div class="api-code-header">
              <div class="api-code-tabs">
                <button class="api-code-tab active" onclick="showCode('alerts', 'curl', event)">cURL</button>
                <button class="api-code-tab" onclick="showCode('alerts', 'python', event)">Python</button>
                <button class="api-code-tab" onclick="showCode('alerts', 'javascript', event)">JavaScript</button>
              </div>
              <button class="api-copy-btn" onclick="copyCode('alerts', event)">Copy</button>
            </div>
            <div class="api-code-content" id="alerts-code-content">
              <div class="api-code-example active" id="alerts-curl">
<pre>curl -X POST "https://api.weather.example/v1/alerts/subscribe" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "location": "New York",
    "webhook_url": "https://example.com/webhook",
    "alert_types": ["storm", "flood"]
  }'</pre>
              </div>
              <div class="api-code-example" id="alerts-python">
<pre>import requests

payload = {
    <span class="key">"location"</span>: <span class="string">"New York"</span>,
    <span class="key">"webhook_url"</span>: <span class="string">"https://example.com/webhook"</span>,
    <span class="key">"alert_types"</span>: [<span class="string">"storm"</span>, <span class="string">"flood"</span>]
}

response = requests.post(
    <span class="string">"https://api.weather.example/v1/alerts/subscribe"</span>,
    json=payload,
    headers={<span class="key">"Authorization"</span>: <span class="string">"Bearer YOUR_API_KEY"</span>}
)

print(response.json())</pre>
              </div>
              <div class="api-code-example" id="alerts-javascript">
<pre>fetch(<span class="string">'https://api.weather.example/v1/alerts/subscribe'</span>, {
  method: <span class="string">'POST'</span>,
  headers: {
    <span class="key">'Authorization'</span>: <span class="string">'Bearer YOUR_API_KEY'</span>,
    <span class="key">'Content-Type'</span>: <span class="string">'application/json'</span>
  },
  body: JSON.stringify({
    location: <span class="string">'New York'</span>,
    webhook_url: <span class="string">'https://example.com/webhook'</span>,
    alert_types: [<span class="string">'storm'</span>, <span class="string">'flood'</span>]
  })
})
  .then(res => res.json())
  .then(data => console.log(data));</pre>
              </div>
            </div>
          </div>

          <h4 style="color:#e8d5d1;margin-top:2rem;font-size:0.9rem;">Response (201 Created)</h4>
          <div class="api-code-block">
            <div class="api-code-content">
<pre>{
  <span class="key">"subscription_id"</span>: <span class="string">"sub_abc123"</span>,
  <span class="key">"location"</span>: <span class="string">"New York, NY"</span>,
  <span class="key">"alert_types"</span>: [<span class="string">"storm"</span>, <span class="string">"flood"</span>],
  <span class="key">"status"</span>: <span class="string">"active"</span>,
  <span class="key">"created_at"</span>: <span class="string">"2024-11-09T14:30:00Z"</span>
}</pre>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

<script>
function showEndpoint(endpointId, event) {
  document.querySelectorAll('.api-endpoint-section').forEach(section => {
    section.classList.remove('active');
  });
  document.querySelectorAll('.api-nav-item').forEach(item => {
    item.classList.remove('active');
  });

  document.getElementById(endpointId).classList.add('active');
  document.getElementById(endpointId + '-examples').classList.add('active');
  event.currentTarget.classList.add('active');
}

function showCode(endpoint, language, event) {
  const container = document.getElementById(endpoint + '-code-content');
  const examples = container.querySelectorAll('.api-code-example');
  const tabs = container.parentElement.querySelectorAll('.api-code-tab');

  examples.forEach(ex => ex.classList.remove('active'));
  tabs.forEach(tab => tab.classList.remove('active'));

  document.getElementById(endpoint + '-' + language).classList.add('active');
  event.currentTarget.classList.add('active');
}

function copyCode(endpoint, event) {
  const container = document.getElementById(endpoint + '-code-content');
  const activeExample = container.querySelector('.api-code-example.active');
  const code = activeExample.textContent;

  navigator.clipboard.writeText(code).then(() => {
    const btn = event.currentTarget;
    const originalText = btn.textContent;
    btn.textContent = 'Copied!';
    setTimeout(() => {
      btn.textContent = originalText;
    }, 2000);
  });
}
</script>
{:/nomarkdown}

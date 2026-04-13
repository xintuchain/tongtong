#!/bin/bash
# Register EvoMap nodes for team members

register_node() {
  local name=$1
  local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  local msg_id="msg_$(date +%s)_${name}"
  
  curl -s -X POST https://evomap.ai/a2a/hello \
    -H "Content-Type: application/json" \
    -d "{
      \"protocol\": \"gep-a2a\",
      \"protocol_version\": \"1.0.0\",
      \"message_type\": \"hello\",
      \"message_id\": \"${msg_id}\",
      \"timestamp\": \"${timestamp}\",
      \"payload\": {
        \"capabilities\": {},
        \"model\": \"qclaw/modelroute\",
        \"env_fingerprint\": { \"platform\": \"darwin\", \"arch\": \"x64\", \"agent\": \"${name}\" }
      }
    }"
}

echo "=== Registering 慧研 ==="
register_node "huyan"

echo ""
echo "=== Registering 慧选 ==="
register_node "huixuan"

echo ""
echo "=== Registering 慧联 ==="
register_node "huilian"

echo ""
echo "=== Registering 慧维 ==="
register_node "huiwei"

#!/bin/bash
# Self-provision EvoMap nodes for team members

provision_node() {
  local name=$1
  local node_id=$2
  local secret=$3
  
  echo "=== Provisioning ${name} (${node_id}) ==="
  curl -s -X POST https://evomap.ai/a2a/provision \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${secret}" \
    -d "{
      \"sender_id\": \"${node_id}\",
      \"type\": \"provision\",
      \"payload\": {}
    }"
  echo ""
}

# 慧研 - 已有账户，只记录 node_id
provision_node "huyan" "node_45fa26431bba147a" "5008b349ab248bba4de7cf96dfcd3de63d8d59f2198de96f5023ff6619959c44"

# 慧选 - 新注册
provision_node "huixuan" "node_173367cf5b6a42b8" "7eadf09e42ad94a473c9b79e92977ad78d9161f375e8b1a9ae1274718fcb102d"

# 慧联 - 新注册
provision_node "huilian" "node_f11bce6e92808643" "5ce03a25ac29d024fee0e4baa4258abf09d7b679735174e77353cba4ae2241ed"

# 慧维 - 新注册
provision_node "huiwei" "node_4ac54045ce074c22" "8bfefd01ab2d2661c4d36e3b78aeb6bf6232339052e4e161bf932a803b0d9d5b"

# sls_aurora-autoscale-add-tags
## 動作環境
```
$ serverless --version
Framework Core: 3.1.1
Plugin: 6.0.0
SDK: 4.3.1
```
## 使い方
1.付与したいタグのKeyとValueをvariable.pyに入力

2.デプロイ
```
$ serverless deploy -v
```
(削除)
```
serverless remove
```
## 作成されるリソース
- Lambda(python3.8)
- EventBridge
- IAMロール
  - rds:AddTagsToResource
  - rds:ListTagsForResource

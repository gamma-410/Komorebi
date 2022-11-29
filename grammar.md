# Grammar
## Hello!
Komorebi は Swift を効率よく書くために開発されました。  
タグ を使用した無駄のない文法で生産性を高めます。  
  
### indention
ハイフン2つで改行を表します。  
これによって余計な改行を減らすことができます。
```go
--
```
### print
print関数は putタグ を使用して表現されます。
```go
put "Hello."
put 1
put 1+1
put 50*100
```
### var
変数は inタグ を使用して定義します。  
Komorebi での定義には記号を使用しません。  
```js
in name String "gamma"
in num Int 500
in float Float 1.23456789
in double Double 1.23456789
in good Bool true
in bad Bool false
```
### let
定数は letタグ を使用して定義します。  
Komorebi での定義には記号を使用しません。  
```js
let userName String "Yuto"
let day Int 31
```
### if / else if / else
条件分岐です。  
波括弧は使用しません。  
セミコロンで条件分岐を閉じます。  
```python
in a Int 10
--
if a<15
    put "aは15よりも小さい。"
;
elif a==15
    put "aは15と等しい。"
;
else
    put "aは15よりも大きい。"
;
```
<?php
/*
 * 其他基础重点笔记
 * 1.函数的命名规则和变量一样，但是函数名不区分大小写
 * 2.在函数内部使用global，表名使用全局变量（不建议使用，破坏了变量完整有效性）；
 *   超级全局变量，在页面的任何部分，包括函数、方法等，都可以直接访问，$_GET、$_POST
 * 3.动态函数：可以用变量的值当函数名
 * 4.获取时间戳:time()、microtime()
 * 5.时间戳格式化：date()
 * 6.解析检测日期：mktime()
 * 7.字符串常识
 * 
 */
header("Content-Type: text/html;charset=utf-8");

/*************时间戳格式化**************/
$time = time();
echo date('Y-m-d 星期N h:i:s', $time);
echo '<br>';
sleep(1);
echo date('Y-m-d 星期N h:i:s');

echo '<br>';
echo date('Y-m-d 星期N h:i:s', 0);
echo '<br>';
echo gmdate('Y-m-d 星期N H:i:s', 0);
echo '<br>';

/*************解析检测日期**************/
echo '<br>';
echo mktime(14,35,20,11,27,2015);
echo '<br>';
echo strtotime('now');
echo '<br>';
echo strtotime('tomorrow');
echo '<br>';
echo strtotime('now + 1 day');
echo '<br>';
var_dump(checkdate(13,2,2000));
var_dump(checkdate(12,2,2000));
echo '<br>';

/*************字符串常识**************/
echo '<br>';
//定义大段文本，可使用heredoc和nowdoc
$str3 = <<<HTML
hello
hjhJFHJHjhl
gshgdshg
yeruyuwmVBNZ
VNbvnb
HTML;
$str4 = <<<BIYJ
hello
hjhJFHJHjhl
gshgdshg,
yeruyuwmVBNZ
VNbvnb
BIYJ;

$str5 = <<<'BIYJ'
hhhhhhhhhhhhh
yyyyyyyyyyyyy
BIYJ;

echo $str3;
echo '<br>';
echo '<br>';
echo $str4;
echo '<br>';

//单双引号:单引号转义的少
echo '<br>';
$str1 = ' \' \\ \n \t \v \$';
echo $str1,'<br>';

$str2 = " \' \\ \n \t \v \$";
echo $str2,'<br>';

//双引号会解析变量值
//单引号比双引号速度要快，因为单引号能转义的字符少，且不需要解析变量的值
$str = 29;
echo '李明今年$str岁','<br>';
echo "李明今年$str岁",'<br>';

//数组键的规则：
//1.如果不声明键，默认会从0,1,2...递增来生成键
//2.如果已经在某一个或者几个数字键，则从最大的数字键，递增生成数字键
//3.如果键声明重复了，后面的值覆盖前面的值
//4.键可以是整数，也可以是字符串；浮点数转成整数，如果字符串的内容恰好是整数，也会理解为整数
$arr = array(2=>'布', 2.5=>'尔', '2'=>'教', '2.5'=>'育');
print_r($arr);


?>
<?php 
$test = 'Pate Bolo';
$test1 = strtolower($test);
$test2 = str_split($test1);
$test3 = str_replace(' ','-',$test2);
// ! foreach ($test2 as $key => $value) {
//     echo $value.'';
// }
echo join($test3)
?>
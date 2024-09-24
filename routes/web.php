<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\pyController;

Route::get('/', function () {
    return view('welcome');
});

// This route will trigger the Python script
Route::get('/python', [pyController::class, 'triggerPython'])->name('python');


Route::get('/run-python', function () {
    $output = [];
    $return_var = 0;

    // Path to your Python script
    $scriptPath = '/app/python/main.py';

    // Execute the Python script
    exec("python3" .escapeshellarg($scriptPath) ."2>&1", $output, $return_var);


    // Check if the execution was successful
    if ($return_var === 0) {
        return response()->json([
            'status' => 'success',
            'output' => $output,
        ]);
    } else {
        return response()->json([
            'status' => 'error',
            'output' => 'Script execution failed!',
        ]);
    }
});

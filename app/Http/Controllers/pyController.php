<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class pyController extends Controller
{
    public function triggerPython()
    {
        $output = [];
        $returnVar = 0;

        // Path to your Python script
        $scriptPath = "C:/Users/FREEZY/Desktop/projects/Laravel Project/run python file/pyLarav/app/python/mainupwork.py";

        // Execute the Python script
        exec("python " . escapeshellarg($scriptPath) . " 2>&1", $output, $returnVar);

        // Log the output and return variable for debugging
        // Log::info('Output: ' . implode("\n", $output));
        // Log::info('Return Var: ' . $returnVar);

        // Return the output as a JSON response
        return response()->json(['output' => $output, 'var' => $returnVar]);
    }
}
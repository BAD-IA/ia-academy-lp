$port = if ($env:PORT) { $env:PORT } else { "5001" }
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()
Write-Host "Listening on http://localhost:$port"
[Console]::Out.Flush()
$root = "F:\CLAUDE CODE\store-lp"
while ($listener.IsListening) {
    $ctx = $listener.GetContext()
    $bytes = [System.IO.File]::ReadAllBytes("$root\index.html")
    $ctx.Response.ContentType = 'text/html; charset=utf-8'
    $ctx.Response.ContentLength64 = $bytes.Length
    $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
    $ctx.Response.OutputStream.Close()
}

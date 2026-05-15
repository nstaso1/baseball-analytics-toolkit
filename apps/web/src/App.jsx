import { useState, useEffect } from 'react'

function App() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    fetch('/api/live-stats')
      .then(res => res.json())
      .then(data => setStats(data))
  }, [])

  if (!stats) return <div>loading baseball analytics...</div>

  return (
    <div>
      <h1>Baseball Live Analytics</h1>
      <div>Inning: {stats.game_status}</div>
      <div>Batter: {stats.current_batter}</div>
      <div>Pitch Velo: {stats.pitch_velocity} mph</div>
      <div>Exit Velo: {stats.exit_velocity} mph</div>
      <div>Launch Angle: {stats.launch_angle} degrees</div>
    </div>
  )
}

export default App

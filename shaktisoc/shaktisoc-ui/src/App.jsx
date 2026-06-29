import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { ShieldAlert, Activity, Network, FileCode, AlertTriangle, Key, Server } from 'lucide-react';

const API_URL = 'http://127.0.0.1:5000/api';

function App() {
  const [status, setStatus] = useState('Initializing Engine...');
  const [data, setData] = useState({
    processes: [], network: [], files: [], logins: [], alerts: []
  });

  useEffect(() => {
    const fetchAllData = async () => {
      try {
        const statRes = await axios.get(`${API_URL}/status`);
        setStatus(statRes.data.status === 'online' ? 'System Secure' : 'Sensors Offline');

        const [proc, net, files, logins, alerts] = await Promise.all([
          axios.get(`${API_URL}/logs/processes`),
          axios.get(`${API_URL}/logs/network`),
          axios.get(`${API_URL}/logs/files`),
          axios.get(`${API_URL}/logs/logins`),
          axios.get(`${API_URL}/logs/alerts`)
        ]);

        setData({
          processes: proc.data.reverse(),
          network: net.data.slice(0, 5),
          files: files.data.slice(0, 5),
          logins: logins.data.slice(0, 5),
          alerts: alerts.data.slice(0, 4)
        });
      } catch (error) {
        setStatus('API Connection Failed');
      }
    };

    fetchAllData();
    const interval = setInterval(fetchAllData, 5000);
    return () => clearInterval(interval);
  }, []);

  const Card = ({ title, icon: Icon, colorClass, children }) => (
    <div className="bg-slate-800 border border-slate-700 rounded-xl shadow-lg p-5 flex flex-col">
      <h3 className="text-slate-200 font-semibold text-sm flex items-center gap-2 mb-4 uppercase tracking-wider">
        <Icon className={colorClass} size={18} /> {title}
      </h3>
      <div className="flex-grow overflow-auto">
        {children}
      </div>
    </div>
  );

  return (
    <div className="min-h-screen p-6 text-slate-300 font-sans">
      
      {/* Top Header */}
      <div className="flex justify-between items-center mb-6 bg-slate-800 p-4 rounded-xl border border-slate-700 shadow-md">
        <div className="flex items-center gap-3">
          <ShieldAlert className="text-blue-500 w-10 h-10" />
          <div>
            <h1 className="text-2xl font-bold text-white leading-tight">ShaktiSOC</h1>
            <p className="text-xs text-slate-400 font-mono">Enterprise Telemetry Engine</p>
          </div>
        </div>
        
        <div className={`flex items-center gap-2 px-4 py-2 rounded-full text-sm font-bold shadow-inner ${status === 'System Secure' ? 'bg-emerald-900/40 text-emerald-400 border border-emerald-800' : 'bg-red-900/40 text-red-400 border border-red-800'}`}>
          <div className={`w-2 h-2 rounded-full animate-pulse ${status === 'System Secure' ? 'bg-emerald-400' : 'bg-red-400'}`}></div>
          {status}
        </div>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        
        {/* ML Alerts - High Priority */}
        <div className="lg:col-span-1">
          <Card title="AI Threat Engine Alerts" icon={AlertTriangle} colorClass="text-rose-500">
            {data.alerts.length === 0 ? (
              <div className="flex flex-col items-center justify-center h-48 text-slate-500">
                <ShieldAlert size={48} className="mb-2 opacity-20" />
                <p>No anomalies detected</p>
              </div>
            ) : (
              <div className="flex flex-col gap-3">
                {data.alerts.map((alert, i) => (
                  <div key={i} className="bg-rose-950/30 border-l-4 border-rose-500 p-3 rounded-r-lg">
                    <div className="text-rose-400 text-xs font-bold mb-1 uppercase tracking-wider">{alert.severity} ALERT</div>
                    <div className="text-sm text-slate-200">{alert.description}</div>
                  </div>
                ))}
              </div>
            )}
          </Card>
        </div>

        {/* CPU Chart */}
        <div className="lg:col-span-2">
          <Card title="Live Resource Telemetry" icon={Activity} colorClass="text-blue-400">
            <div className="h-64 w-full">
              <ResponsiveContainer>
                <LineChart data={data.processes}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#334155" vertical={false} />
                  <XAxis dataKey="process_name" stroke="#64748b" tick={{fontSize: 12}} tickMargin={10} />
                  <YAxis stroke="#64748b" tick={{fontSize: 12}} />
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155', color: '#f8fafc', borderRadius: '8px' }}
                    itemStyle={{ color: '#60a5fa' }}
                  />
                  <Line type="monotone" dataKey="cpu_usage" stroke="#3b82f6" strokeWidth={2} dot={false} isAnimationActive={false} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </Card>
        </div>
      </div>

      {/* Bottom Grid for Logs */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card title="Authentication Logs" icon={Key} colorClass="text-amber-400">
          <table className="w-full text-sm text-left">
            <tbody>
              {data.logins.map((log, i) => (
                <tr key={i} className="border-b border-slate-700/50 hover:bg-slate-700/20 transition-colors">
                  <td className="py-3 font-medium text-slate-300">{log.username}</td>
                  <td className="py-3 text-slate-500 font-mono text-xs">{log.source_ip}</td>
                  <td className={`py-3 text-right font-bold ${log.status === 'SUCCESS' ? 'text-emerald-400' : 'text-rose-500'}`}>{log.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>

        <Card title="Network Socket States" icon={Network} colorClass="text-purple-400">
          <table className="w-full text-sm text-left">
            <tbody>
              {data.network.map((log, i) => (
                <tr key={i} className="border-b border-slate-700/50 hover:bg-slate-700/20 transition-colors">
                  <td className="py-3 text-purple-400 font-mono text-xs">{log.protocol}</td>
                  <td className="py-3 text-slate-300">{log.remote_ip}:{log.remote_port}</td>
                  <td className={`py-3 text-right text-xs font-bold ${log.status === 'ESTABLISHED' ? 'text-emerald-400' : 'text-amber-400'}`}>{log.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>

        <Card title="File Integrity Monitor" icon={FileCode} colorClass="text-pink-400">
          <table className="w-full text-sm text-left table-fixed">
            <tbody>
              {data.files.map((file, i) => (
                <tr key={i} className="border-b border-slate-700/50 hover:bg-slate-700/20 transition-colors">
                  <td className={`py-3 w-24 text-xs font-bold ${file.action_type === 'DELETED' ? 'text-rose-400' : 'text-blue-400'}`}>{file.action_type}</td>
                  <td className="py-3 text-slate-400 truncate font-mono text-xs" title={file.file_path}>
                    {file.file_path}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      </div>

    </div>
  );
}

export default App;
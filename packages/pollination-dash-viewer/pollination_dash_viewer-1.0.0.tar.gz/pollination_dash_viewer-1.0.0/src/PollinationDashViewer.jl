
module PollinationDashViewer
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.0.0"

include("jl/''_vtkdashviewer.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "pollination_dash_viewer",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "pollination_dash_viewer.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "pollination_dash_viewer.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
